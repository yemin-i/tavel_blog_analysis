#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re
import json # 네이버 api는 xml과 json 형태로 제공하기 때문에 json 처리 라이브러리 호출
import math
import requests
import urllib.request
import urllib.error
import urllib.parse
from bs4 import BeautifulSoup
import pandas as pd


# In[2]:


naver_client_id = id
naver_client_secret = password


# In[3]:


# 검색한 키워드에 해당하는 전체 블로그 갯수를 가져오는 함수
def get_blog_count(query, display):  # query 부분에 검색어가 들어감
    encode_query = urllib.parse.quote(query)
    search_url = "https://openapi.naver.com/v1/search/blog?query=" + encode_query
    request = urllib.request.Request(search_url)

    request.add_header("X-Naver-Client-Id", naver_client_id)
    request.add_header("X-Naver-Client-Secret", naver_client_secret)

    response = urllib.request.urlopen(request) # url에 해당하는 결과 요청
    response_code = response.getcode()  # 결과요청에 대한 코드 반환(200 : 제대로 처리)

    if response_code is 200:
        response_body = response.read()
        response_body_dict = json.loads(response_body.decode('utf-8')) # json형태의 데이터를 처리하기 위해 json 로드

        print("Last build date: " + str(response_body_dict['lastBuildDate'])) # 검색결과를 생성한 시간
        print("Total: " + str(response_body_dict['total']))                   # 검색 결과 문서의 총 개수
        print("Start: " + str(response_body_dict['start']))                   # 검색 결과 문서 중, 문서의 시작점
        print("Display: " + str(response_body_dict['display']))               # 검색된 검색 결과의 개수

        if response_body_dict['total'] == 0:
            blog_count = 0
        else:
            blog_total = math.ceil(response_body_dict['total'] / int(display))

            if blog_total >= 1000: # 최대 블로그 검색결과는 1000개이므로
                blog_count = 1000 # 1000개 이상일 경우, 블로그 개수를 1000개로 맞춰줌
            else:
                blog_count = blog_total

            print("Blog total: " + str(blog_total))
            print("Blog count: " + str(blog_count))

        return blog_count


# In[4]:


# 검색된 블로그의 내용을 가져오기 위한 함수

# display == 검색 결과 출력 건수를 지정하는 데 사용되며 기본 값이 10이고, 최대 100개까지 지정
# start == 검색 시작 위치로 1부터 최대 1000까지 가능
# sort == 정렬옵션으로 sim(유사도), date(날짜순)으로 지정 가능

def get_blog_post(query, display, start_index, sort):
    global no, df
    
    encode_query = urllib.parse.quote(query)
    search_url = "https://openapi.naver.com/v1/search/blog?query=" + encode_query + "&display=" + str(display) + "&start=" + str(start_index) + "&sort=" + sort

    request = urllib.request.Request(search_url)

    request.add_header("X-Naver-Client-Id", naver_client_id)
    request.add_header("X-Naver-Client-Secret", naver_client_secret)

    response = urllib.request.urlopen(request)
    response_code = response.getcode()

    if response_code is 200:
        response_body = response.read()
        response_body_dict = json.loads(response_body.decode('utf-8'))
        for item_index in range(0, len(response_body_dict['items'])):
            try:
                remove_html_tag = re.compile('<.*?>') # HTML 태그를 제거하기 위해 정규표현식 함수 이용
                title = re.sub(remove_html_tag, '', response_body_dict['items'][item_index]['title'])
                link = response_body_dict['items'][item_index]['link'].replace("amp;", "")
                description = re.sub(remove_html_tag, '', response_body_dict['items'][item_index]['description'])
                blogger_name = response_body_dict['items'][item_index]['bloggername']
                blogger_link = response_body_dict['items'][item_index]['bloggerlink']
                
                post_date = response_body_dict['items'][item_index]['postdate'] # 날짜 형식으로 변환
                
                # 네이버 검색 api로는 일부 내용만 반환하고, 블로그의 전체 내용을 가져올 수 없다. 그러므로 BeautifulSoup 라이브러리를
                # 이용하여 실제 블로그 주소로 접속하여 포스트 내용을 가져와서 파일에 저장한다

                no += 1
                post_code = requests.get(link)
                post_text = post_code.text
                post_soup = BeautifulSoup(post_text, 'lxml')

                blog_post_content_text = ""
                for mainFrame in post_soup.select('iframe#mainFrame'):
                    blog_post_url = "http://blog.naver.com" + mainFrame.get('src')
                    blog_post_code = requests.get(blog_post_url)
                    blog_post_text = blog_post_code.text
                    blog_post_soup = BeautifulSoup(blog_post_text, 'lxml')
                    
                    for blog_post_content in blog_post_soup.find_all('div', class_='se-viewer'):
                        blog_post_content_text = blog_post_content.get_text()
                        
                    for blog_post_content in blog_post_soup.find_all('div', class_='se_doc_viewer'):
                        blog_post_content_text = blog_post_content.get_text()
 
                    for blog_post_content in blog_post_soup.select('div#postViewArea'):
                        blog_post_content_text = blog_post_content.get_text()

                df.loc[no] = [title, link, description, blogger_name, blogger_link, post_date, blog_post_content_text]
                print("#", end='')
                
            except:
                item_index += 1


# In[5]:


no = 0                 # 몇개의 포스트를 저장하였는지 세기 위한 index
query = "국내여행 +혼자 -가족,친구"   # 검색을 원하는 문자열로서 UTF-8로 인코딩한다.
display = 10           # 검색 결과 출력 건수 지정, 10(기본값),100(최대)
start = 1              # 검색 시작 위치로 최대 1000까지 가능
sort = "sim"           # 정렬 옵션: sim(유사도순, 기본값), date(날짜순)

# 블로그를 DataFrame에 저장
df = pd.DataFrame(columns=("Title", "Link", "Description", "Blogger Name", "Blogger Link", "Post Date", "Post Contents"))

blog_count = get_blog_count(query, display)
for start_index in range(start, blog_count + 1, display): # get_blog_counts() 함수를 통해 알아 낸 블로그의 전체 수만큼 get_blog_post()
    get_blog_post(query, display, start_index, sort)       # 함수 반복 수행

df.to_csv("travel_crawl.csv", header=True, index=False)


# In[ ]:




