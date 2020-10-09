#!/usr/bin/env python
# coding: utf-8

# <h1>Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#혼행족이-선호하는-여행지-분석" data-toc-modified-id="혼행족이-선호하는-여행지-분석-1"><center>혼행족이 선호하는 여행지 분석</center></a></span></li><li><span><a href="#1.-프로젝트-개요" data-toc-modified-id="1.-프로젝트-개요-2">1. 프로젝트 개요</a></span><ul class="toc-item"><li><span><a href="#1.1-데이터-수집" data-toc-modified-id="1.1-데이터-수집-2.1">1.1 데이터 수집</a></span></li><li><span><a href="#1.2-개발-환경" data-toc-modified-id="1.2-개발-환경-2.2">1.2 개발 환경</a></span></li><li><span><a href="#1.3-라이브러리" data-toc-modified-id="1.3-라이브러리-2.3">1.3 라이브러리</a></span></li><li><span><a href="#1.4-데이터-로드" data-toc-modified-id="1.4-데이터-로드-2.4">1.4 데이터 로드</a></span></li></ul></li><li><span><a href="#2.-전처리" data-toc-modified-id="2.-전처리-3">2. 전처리</a></span><ul class="toc-item"><li><span><a href="#2.1-소문자-변환" data-toc-modified-id="2.1-소문자-변환-3.1">2.1 소문자 변환</a></span></li><li><span><a href="#2.2-개행문자-제거" data-toc-modified-id="2.2-개행문자-제거-3.2">2.2 개행문자 제거</a></span></li><li><span><a href="#2.3-한글-추출" data-toc-modified-id="2.3-한글-추출-3.3">2.3 한글 추출</a></span></li><li><span><a href="#2.4-Stop-Word" data-toc-modified-id="2.4-Stop-Word-3.4">2.4 Stop Word</a></span></li><li><span><a href="#2.5-품사-추출" data-toc-modified-id="2.5-품사-추출-3.5">2.5 품사 추출</a></span><ul class="toc-item"><li><span><a href="#2.5.1-명사" data-toc-modified-id="2.5.1-명사-3.5.1">2.5.1 명사</a></span></li><li><span><a href="#2.5.2-동사" data-toc-modified-id="2.5.2-동사-3.5.2">2.5.2 동사</a></span></li><li><span><a href="#2.5.3-형용사" data-toc-modified-id="2.5.3-형용사-3.5.3">2.5.3 형용사</a></span></li></ul></li></ul></li><li><span><a href="#3.-자연어처리" data-toc-modified-id="3.-자연어처리-4">3. 자연어처리</a></span><ul class="toc-item"><li><span><a href="#3.1-BOW(Bag-Of-Word)" data-toc-modified-id="3.1-BOW(Bag-Of-Word)-4.1">3.1 BOW(Bag Of Word)</a></span></li><li><span><a href="#3.2-어휘-빈도---문서-역빈도(TF-IDF)" data-toc-modified-id="3.2-어휘-빈도---문서-역빈도(TF-IDF)-4.2">3.2 어휘 빈도 - 문서 역빈도(TF-IDF)</a></span></li></ul></li><li><span><a href="#4.-사회연결망분석(SNA)" data-toc-modified-id="4.-사회연결망분석(SNA)-5">4. 사회연결망분석(SNA)</a></span><ul class="toc-item"><li><span><a href="#4.1-연결-중심성" data-toc-modified-id="4.1-연결-중심성-5.1">4.1 연결 중심성</a></span></li><li><span><a href="#4.2-위세-중심성" data-toc-modified-id="4.2-위세-중심성-5.2">4.2 위세 중심성</a></span></li><li><span><a href="#4.3-근접-중심성" data-toc-modified-id="4.3-근접-중심성-5.3">4.3 근접 중심성</a></span></li><li><span><a href="#4.4-매개-중심성" data-toc-modified-id="4.4-매개-중심성-5.4">4.4 매개 중심성</a></span></li><li><span><a href="#4.5-중심성(종합)" data-toc-modified-id="4.5-중심성(종합)-5.5">4.5 중심성(종합)</a></span></li><li><span><a href="#4.6-네트워크-그림" data-toc-modified-id="4.6-네트워크-그림-5.6">4.6 네트워크 그림</a></span></li><li><span><a href="#4.7-커뮤니티-탐지" data-toc-modified-id="4.7-커뮤니티-탐지-5.7">4.7 커뮤니티 탐지</a></span></li></ul></li><li><span><a href="#5.-군집분석" data-toc-modified-id="5.-군집분석-6">5. 군집분석</a></span></li><li><span><a href="#6.-유사도" data-toc-modified-id="6.-유사도-7">6. 유사도</a></span><ul class="toc-item"><li><span><a href="#6.1-문서-간-유사도" data-toc-modified-id="6.1-문서-간-유사도-7.1">6.1 문서 간 유사도</a></span></li><li><span><a href="#6.2-단어-간-유사도" data-toc-modified-id="6.2-단어-간-유사도-7.2">6.2 단어 간 유사도</a></span></li></ul></li><li><span><a href="#7.-추천-시스템" data-toc-modified-id="7.-추천-시스템-8">7. 추천 시스템</a></span><ul class="toc-item"><li><span><a href="#7.1-아이템-기반-여행지-추천" data-toc-modified-id="7.1-아이템-기반-여행지-추천-8.1">7.1 아이템 기반 여행지 추천</a></span></li><li><span><a href="#7.2-유사-여행지-추천" data-toc-modified-id="7.2-유사-여행지-추천-8.2">7.2 유사 여행지 추천</a></span></li></ul></li><li><span><a href="#8.-종합결과" data-toc-modified-id="8.-종합결과-9">8. 종합결과</a></span><ul class="toc-item"><li><span><a href="#8.1-TF-IDF" data-toc-modified-id="8.1-TF-IDF-9.1">8.1 TF-IDF</a></span></li><li><span><a href="#8.2-중심성" data-toc-modified-id="8.2-중심성-9.2">8.2 중심성</a></span></li><li><span><a href="#8.3-네트워크-그림" data-toc-modified-id="8.3-네트워크-그림-9.3">8.3 네트워크 그림</a></span></li><li><span><a href="#8.4-단어-간-유사도" data-toc-modified-id="8.4-단어-간-유사도-9.4">8.4 단어 간 유사도</a></span></li><li><span><a href="#8.5-여행지-추천시스템" data-toc-modified-id="8.5-여행지-추천시스템-9.5">8.5 여행지 추천시스템</a></span></li></ul></li></ul></div>

# # <center>혼행족이 선호하는 여행지 분석</center>

# * 분석자 : 이재성
#     
#     
# * 분석기간 : 2020년 8월 ~ 9월

# <h1>Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#혼행족이-선호하는-여행지-분석" data-toc-modified-id="혼행족이-선호하는-여행지-분석-1"><center>혼행족이 선호하는 여행지 분석</center></a></span></li><li><span><a href="#1.-프로젝트-개요" data-toc-modified-id="1.-프로젝트-개요-2">1. 프로젝트 개요</a></span><ul class="toc-item"><li><span><a href="#1.1-데이터-수집" data-toc-modified-id="1.1-데이터-수집-2.1">1.1 데이터 수집</a></span></li><li><span><a href="#1.2-개발-환경" data-toc-modified-id="1.2-개발-환경-2.2">1.2 개발 환경</a></span></li><li><span><a href="#1.3-라이브러리" data-toc-modified-id="1.3-라이브러리-2.3">1.3 라이브러리</a></span></li><li><span><a href="#1.4-데이터-로드" data-toc-modified-id="1.4-데이터-로드-2.4">1.4 데이터 로드</a></span></li></ul></li><li><span><a href="#2.-전처리" data-toc-modified-id="2.-전처리-3">2. 전처리</a></span><ul class="toc-item"><li><span><a href="#2.1-소문자-변환" data-toc-modified-id="2.1-소문자-변환-3.1">2.1 소문자 변환</a></span></li><li><span><a href="#2.2-개행문자-제거" data-toc-modified-id="2.2-개행문자-제거-3.2">2.2 개행문자 제거</a></span></li><li><span><a href="#2.3-한글-추출" data-toc-modified-id="2.3-한글-추출-3.3">2.3 한글 추출</a></span></li><li><span><a href="#2.4-Stop-Word" data-toc-modified-id="2.4-Stop-Word-3.4">2.4 Stop Word</a></span></li><li><span><a href="#2.5-품사-추출" data-toc-modified-id="2.5-품사-추출-3.5">2.5 품사 추출</a></span><ul class="toc-item"><li><span><a href="#2.5.1-명사" data-toc-modified-id="2.5.1-명사-3.5.1">2.5.1 명사</a></span></li><li><span><a href="#2.5.2-동사" data-toc-modified-id="2.5.2-동사-3.5.2">2.5.2 동사</a></span></li><li><span><a href="#2.5.3-형용사" data-toc-modified-id="2.5.3-형용사-3.5.3">2.5.3 형용사</a></span></li></ul></li></ul></li><li><span><a href="#3.-자연어처리" data-toc-modified-id="3.-자연어처리-4">3. 자연어처리</a></span><ul class="toc-item"><li><span><a href="#3.1-BOW(Bag-Of-Word)" data-toc-modified-id="3.1-BOW(Bag-Of-Word)-4.1">3.1 BOW(Bag Of Word)</a></span></li><li><span><a href="#3.2-어휘-빈도---문서-역빈도(TF-IDF)" data-toc-modified-id="3.2-어휘-빈도---문서-역빈도(TF-IDF)-4.2">3.2 어휘 빈도 - 문서 역빈도(TF-IDF)</a></span></li></ul></li><li><span><a href="#4.-사회연결망분석(SNA)" data-toc-modified-id="4.-사회연결망분석(SNA)-5">4. 사회연결망분석(SNA)</a></span><ul class="toc-item"><li><span><a href="#4.1-연결-중심성" data-toc-modified-id="4.1-연결-중심성-5.1">4.1 연결 중심성</a></span></li><li><span><a href="#4.2-위세-중심성" data-toc-modified-id="4.2-위세-중심성-5.2">4.2 위세 중심성</a></span></li><li><span><a href="#4.3-근접-중심성" data-toc-modified-id="4.3-근접-중심성-5.3">4.3 근접 중심성</a></span></li><li><span><a href="#4.4-매개-중심성" data-toc-modified-id="4.4-매개-중심성-5.4">4.4 매개 중심성</a></span></li><li><span><a href="#4.5-중심성(종합)" data-toc-modified-id="4.5-중심성(종합)-5.5">4.5 중심성(종합)</a></span></li><li><span><a href="#4.6-네트워크-그림" data-toc-modified-id="4.6-네트워크-그림-5.6">4.6 네트워크 그림</a></span></li><li><span><a href="#4.7-커뮤니티-탐지" data-toc-modified-id="4.7-커뮤니티-탐지-5.7">4.7 커뮤니티 탐지</a></span></li></ul></li><li><span><a href="#5.-군집분석" data-toc-modified-id="5.-군집분석-6">5. 군집분석</a></span></li><li><span><a href="#6.-유사도" data-toc-modified-id="6.-유사도-7">6. 유사도</a></span><ul class="toc-item"><li><span><a href="#6.1-문서-간-유사도" data-toc-modified-id="6.1-문서-간-유사도-7.1">6.1 문서 간 유사도</a></span></li><li><span><a href="#6.2-단어-간-유사도" data-toc-modified-id="6.2-단어-간-유사도-7.2">6.2 단어 간 유사도</a></span></li></ul></li><li><span><a href="#7.-추천-시스템" data-toc-modified-id="7.-추천-시스템-8">7. 추천 시스템</a></span><ul class="toc-item"><li><span><a href="#7.1-아이템-기반-여행지-추천" data-toc-modified-id="7.1-아이템-기반-여행지-추천-8.1">7.1 아이템 기반 여행지 추천</a></span></li><li><span><a href="#7.2-유사-여행지-추천" data-toc-modified-id="7.2-유사-여행지-추천-8.2">7.2 유사 여행지 추천</a></span></li></ul></li><li><span><a href="#8.-종합결과" data-toc-modified-id="8.-종합결과-9">8. 종합결과</a></span><ul class="toc-item"><li><span><a href="#8.1-TF-IDF" data-toc-modified-id="8.1-TF-IDF-9.1">8.1 TF-IDF</a></span></li><li><span><a href="#8.2-중심성" data-toc-modified-id="8.2-중심성-9.2">8.2 중심성</a></span></li><li><span><a href="#8.3-네트워크-그림" data-toc-modified-id="8.3-네트워크-그림-9.3">8.3 네트워크 그림</a></span></li><li><span><a href="#8.4-단어-간-유사도" data-toc-modified-id="8.4-단어-간-유사도-9.4">8.4 단어 간 유사도</a></span></li><li><span><a href="#8.5-여행지-추천시스템" data-toc-modified-id="8.5-여행지-추천시스템-9.5">8.5 여행지 추천시스템</a></span></li></ul></li></ul></div>

# # 1. 프로젝트 개요

# 몇년 전부터 혼밥, 혼술, 혼행 등 혼자 하는 콘텐츠가 많아지고 있는 추세입니다. 이 중, 혼행(혼자 여행)에 초점을 맞춰 혼행족들이 선호하는 여행지를 살펴보고 그 여행지가 가지는 특징을 살펴보고자 합니다. 유사도 분석을 바탕으로 혼행이 아니더라도 여행을 계획하는 사람들에게 여행지와 관련된 인기 장소, 먹거리 등 지역 관련된 다양한 키워드를 제시하고자 합니다. 마지막으로 코사인 유사도를 활용한 여행지 추천시스템을 구현하여 선호하는 키워드를 입력하면 특정 여행지를 추천해주는 기능도 구현하고자 합니다.

# ## 1.1 데이터 수집

# * 데이터 : 네이버 블로그 본문 1000개 (네이버 API를 통한 크롤링)
# 
#     
# * 검색어 : '국내여행 +혼자 -가족,친구'
# 
# 
# * 수집일 : 2020년 7월 15일 
# 
# 
# * 검색방식 : 정확도 기반 검색

# ## 1.2 개발 환경

# pandas == 1.0.5
# 
# numpy == 1.18.5
# 
# matplotlib == 3.2.2
# 
# seaborn == 0.10.1
# 
# eunjeon == 0.4.0
# 
# re == 2.2.1
# 
# sklearn == 0.23.1
# 
# networkx == 2.4
# 
# community == 0.14
# 
# gensim == 3.8.3

# ## 1.3 라이브러리
# 
# * 현재 항목에서는 기본적인 라이브러리만을 정리했습니다.

# In[1]:


import pandas as pd
import numpy as np
from collections import Counter # 갯수 파악 라이브러리
from eunjeon import Mecab       # 자연어 처리 라이브러리
import matplotlib.pyplot as plt
import seaborn as sns
import re

plt.rc('font', family='Malgun Gothic')
pd.options.display.max_columns = 50  # 컬럼 출력 개수 설정
get_ipython().run_line_magic('matplotlib', 'inline')


# ## 1.4 데이터 로드

# In[2]:


data = pd.read_csv('travel_crawl.csv')

print(data.shape)
data.head()


# In[3]:


# 컬럼 이름 정리(언더바 삽입)
data.columns = ['Title', 'Link', 'Description', 'Blogger_Name', 'Blogger_Link', 'Post_Date', 'Post_Contents']

data.head()


# In[4]:


# 네트워크 오류 등으로 발생한 중복 입력 값을 제거하겠습니다.

print('원본 포스팅 글 수 :',data.shape)

data = data.drop_duplicates(['Post_Contents'], keep = 'last') # 가장 최근 내용을 남기겠습니다.

print('중복 제거 후 포스팅 글 수 :', data.shape)
data.head()


# **중복된 포스팅 글 18개를 제거한 총 982개의 포스팅 글을 분석에 활용하겠습니다.**

# In[5]:


# 원본은 따로 보관하겠습니다.

data['raw_Post_Contents'] = data['Post_Contents']


# # 2. 전처리

# ## 2.1 소문자 변환

# In[6]:


# 파이썬에서는 대문자와 소문자를 따로 처리하므로 Post_Contents에 포함된 영어는 모두 소문자로 변환하겠습니다.
data['Post_Contents'] = data['Post_Contents'].str.lower()


# In[7]:


data.head()


# ## 2.2 개행문자 제거

# In[8]:


# 개행문자를 제거하여 contents 라는 리스트에 담겠습니다.

contents = []
posts = data['Post_Contents']
for post in posts:
    post = str(post).replace('\n','').replace('\u200b','').replace('\xa0','').replace('\t','')
    contents.append(str(post))

contents[1]


# **현재, 본문 내용 중 이모티콘이 제거되지 않았습니다. 아래에서 한글만을 남기고 다른 문자는 모두 제거하겠습니다.**

# ## 2.3 한글 추출

# In[9]:


# 내용 중 한글만을 추출하는 함수를 만들겠습니다.

def extract_hangeul(x):
    han_contents = []

    for i in contents:
        text = re.sub('[^ㄱ-ㅎㅏ-ㅣ가-힣 ]',' ',i).lstrip()

        if(text != ''):
            han_contents.append(text)

    return han_contents

han_contents = extract_hangeul(contents)

han_contents[1]


# **한글을 제외한 모든 문자가 제거되었습니다.**

# In[10]:


# 본 프로젝트에서는 KoNLPy에서 제공하는 다섯 가지의 자연어처리기 중 은전한잎(Mecab)을 사용하겠습니다.

mecab = Mecab()


# ## 2.4 Stop Word

# In[11]:


# stop word(불용어)를 지정하겠습니다.
# stop word에는 혼자와는 반대되는 관계 등의 단어(가족, 친구 등), 조사, 이외 본 프로젝트 목적과 관련없는 단어를 포함시켰습니다. 

stop_words = '이웃 추가 환영 댓글 공감 본문 기타 복사 기능 번역 이웃추가본문 박일 기타 복사 기능지도로 기능번역보기 지도닫기 전체지도 번역보기 몸 뭐 한국 빠 픽 힙 동안 가능 여행지 모습 어디 마음 가족 위치 기능 추가 지도 기타 이용 위치 장소 복사 본문 번역 우리 도착 이번 여기 하나 정도 다음 이곳 느낌 때문 코레 끼 플라 이젠 아무것 앤 림 순 노 뭘 유럽 부 동행 팩족 빈이 화 조 부분 뭐 안녕 밖 뭔가 백 경우 적 샷 해외여행 해외 만큼 땐 텐데 맘 겁니다 그때 난 무엇 이게 지 살 반 일본 이건 완전 던분 신랑 이거 너 얼마 선 간 턴 곳곳 켄싱 나중 애 대부분 오 언니 부모 이것 밑 땅 겸 거기 건지 조금 관련 색 그곳 여러분 커플 이후 마련 덕분상세 자기 외 둘째 힘 누구 그것 씨 결국 테 컷 그 저기 운 급 미 등등 초 세 핫 관 포함 연인 도 팀 여긴 당시 지인 리뷰 면 법 척 뜻공 떼 탄 건데 바 열 할머니 요기 군데 뿐 찜 뻔 ㄷ 식 덕 텐데요 셋 그게 꺼 포 채 청 굿 칸 어딜 주요 아저씨 막 유 용 실 병 정 권 킹쪽 존 군 빈 걸 저희 점 명 호 대 둘 주 남 후 제 안 앞 뒤 건 데 천 층 편 끝 줄 옆 속 위 아래 네 내 게 년 날 중 듯 은 이 것 등 더 를좀 즉 인 옹 때 만 원 이때 개 일 기 시 럭 갤 성 삼 스 폰 트 드 기 이 리 사 전 마 자 플 가 박 짱 어머니 아버지 엄마 아빠 동생 아들 딸아기 아가 아이 분 남편 이웃 수 곳 거 번 월 저 나 한때 쓰리 현과 현정 쓰 무튼 주노 그날 웡 가지 확인 저장 아기 현빈'

stop_words = stop_words.split(' ')
stop_words[0:10]


# ## 2.5 품사 추출

# In[12]:


# 형태소 분석은 단어가 의미하는 형태를 찾아주어 원형에 대한 부분만 추출할 수 있습니다.
# pos 함수를 사용해 품사를 추출하겠습니다.
# 품사 추출 함수를 만들어 출력하겠습니다.

def extract_pos(x):
    words = []
    for content in x:
        words.extend(mecab.pos(content))  # tagger의 품사(part of speech : POS)
    return words
    
word_pos = extract_pos(han_contents)
word_pos[:10]


# ### 2.5.1 명사

# In[13]:


# 포스팅 글(contents)에서 명사를 추출하는 함수를 만들어 출력하겠습니다.
# 이때, stop_words 리스트에 없는 명사만 nouns 리스트에 담겠습니다. 

def extract_noun(x):
    nouns = []
    for content in x:
        for noun in mecab.nouns(content):
            if noun not in stop_words:
                nouns.append(noun)
    return nouns
nouns = extract_noun(han_contents)
nouns[:10]


# ### 2.5.2 동사

# In[14]:


# 동사를 추출하는 함수를 만들겠습니다.
# 추출을 위해 형태소 분석을 한 결과에서 동사(VV)에 해당하는 형태에 '다'를 추가하겠습니다.

def extract_verb(x):
    verbs = []
    for word in x:
        if word[1] == 'VV':
            verbs.append(word[0] + '다')
    return verbs
        
verbs = extract_verb(word_pos)
verbs[0:10]


# ### 2.5.3 형용사

# In[15]:


# 형용사를 추출하는 함수를 만들겠습니다.
# 추출을 위해 형태소 분석을 한 결과에서 형용사(VA)에 해당하는 형태에 '다'를 추가하겠습니다.

def extract_adj(x):
    adjective = []
    for word in x:
        if word[1] == 'VA':
            adjective.append(word[0] + '다')
    return adjective

adjective = extract_adj(word_pos)
adjective[0:10]


# In[16]:


# 300개(임의 지정)의 단어에 대한 빈도를 추출하겠습니다.

num_top_nouns = 300
travel_noun_count = Counter(nouns)

# most_common() : 데이터의 개수가 많은 순으로 정렬된 배열을 리턴하는 메서드
travel_top_nouns = dict(travel_noun_count.most_common(num_top_nouns))

sorted(travel_top_nouns.items(), key=lambda x: x[1], reverse=True)[:10]


# **추출된 명사의 빈도별로 살펴보면, 여행, 국내, 사진, 시간, 길, 생각 등의 단어의 빈도가 가장 높았습니다.**

# # 3. 자연어처리

# ## 3.1 BOW(Bag Of Word)

# * 군집을 만들기 위해 가장 적절한 방법은 게시물마다 등장하는 단어의 빈도수를 파악해 하나의 카운트 벡터로 만듭니다. 이를 단어 주머니 접근 법이라고 합니다. 카운트 벡터 생성 후 해당 게시물과 다른 게시물 사이의 벡터 거리를 계산하여 게시물 사이의 유사도를 파악하면 됩니다.

# In[17]:


# BOW 단어 가방에 단어를 토큰화해서 담겠습니다.
# 기본적으로 CountVectorizer 는 1글자 단어를 제거하여 출력합니다.

from sklearn.feature_extraction.text import CountVectorizer

vectorizer = CountVectorizer(analyzer = 'word',        # 단어 단위로 벡터화
                            tokenizer = None,         # 별도의 토크나이저를 지정하지 않음
                            preprocessor = None,      # 전처리 도구
                            stop_words = stop_words,  # 불용어 지정
                            max_features = 50000)     # 만들 단어의 수 50000개

print(vectorizer.fit_transform(travel_top_nouns).toarray()) 
print(sorted(vectorizer.vocabulary_.items()))


# In[18]:


# vectorizer가 travel_top_nouns 를 학습하도록 하겠습니다.

travel_top_nouns_vector = vectorizer.fit(travel_top_nouns)

travel_top_nouns_vector


# In[19]:


# 변환된 travel_top_nouns 261개의 단어 * 982개의 문서 간의 array 형태를 DataFrame 형태로 출력하겠습니다. 

doc_word_df = pd.DataFrame(travel_top_nouns_vector.transform(contents).toarray())

doc_word_df


# In[20]:


# get_feature_names() 메소드를 통해 생성한 피처를 가져와 출력하겠습니다.
vocab = vectorizer.get_feature_names()  
print(len(vocab))

# 261개의 단어와 인덱스 값을 쌍으로 출력하겠습니다.
vocab_dict = vectorizer.vocabulary_ 
sorted(vocab_dict.items(), key=lambda x: x[1], reverse=False)[:10]


# In[21]:


# 위의 행렬에서 각 컬럼 숫자와 매핑되는 단어로 변환하겠습니다.
# 각 블로그 본문마다 등장하는 단어의 빈도를 출력하겠습니다.

vocab_df = pd.DataFrame(travel_top_nouns_vector.transform(contents).toarray(), columns = vocab)

vocab_df


# In[22]:


# 위에서 구한 단어벡터를 더하면 단어가 전체에서 등장하는 횟수를 알 수 있습니다.
# 벡터화된 피처를 확인하여 Bag Of Word에 저장된 단어 빈도를 확인하겠습니다.

df_frequency = pd.DataFrame(np.sum(vocab_df))

df_frequency.columns = ['freq']

print(len(df_frequency))
df_frequency.sort_values(by = 'freq', ascending = False).head(20)


# In[23]:


# 위의 행렬에서 가장 빈도가 높은 단어와 빈도를 출력하겠습니다.

max_freq = 0
word = None

for i in range(len(df_frequency['freq'])):
    if df_frequency['freq'][i] > max_freq:
        max_freq = df_frequency['freq'][i]
        word = list(df_frequency.index)[i]

print(f'가장 빈도가 높은 단어 : {word}, 빈도 : {max_freq}')


# **Counter 라이브러리의 mecab.nouns() 함수를 사용했을 때의 결과는 복합명사(양양여행)를 하나로 보지 않고 '양양'과 '여행'으로 따로 빈도를 세었기 때문에 BOW 빈도와는 차이가 있습니다. 본 프로젝트에서는 Counter 라이브러리 활용 결과는 단순 상위 300개의 빈도만을 추출하기 위한 목적으로 사용되었습니다.**
# 
# **BOW 처리 과정에서는 300개의 단어를 활용하여 해당 단어가 블로그 내용 내에 몇 번 등장했는지를 기초로 매트릭스가 출력되었습니다.**
# 
# * BOW 결과를 간략히 정리하면 다음과 같습니다.
# 
# 
#     - 1. 빈도가 가장 높은 단어는 여행(1374)으로 나타났습니다. 다음으로, 혼자(1185), 사진(669), 국내(604), 추천(469) 등의 순으로 빈도가 높았습니다.
#     
#     - 2. 자주 등장한 지역을 살펴보면, 제주도(324)가 가장 많았습니다. 다음으로, 경주(292), 강원도(291), 여수(254), 부산(226), 강릉(204) 등으로 나타났습니다.

# ## 3.2 어휘 빈도 - 문서 역빈도(TF-IDF)
# 
# * TF : 특정한 단어가 현재 문서 내에 얼마나 자주 등장하는지(단어의 빈도수)를 나타낸 값으로, 이 값이 높을수록 문서에서 중요하다고 생각하는 개념입니다.
# 
# 
# * 빈도가 높다고 텍스트의 주제를 잘 드러내는 핵심어라고 보기 어렵습니다. 그 어휘가 다른 문서에는 별로 등장하지 않고 특정 문서에만 집중적으로 등장 할 때 그 어휘야말로 실질적으로 그 문서의 주제를 잘 담고 있는 핵심어라 할 수 있습니다. 특정 문서에서 특정 단어가 많이 등장하는 빈도가 많으면서 동시에 그 단어가 다른 문서에서 등장하는 빈도가 적을 때, 특정 문서의 핵심어로 간주합니다.
# 
# 
# * 단어 자체가 전체 문서 내에서 자주 사용되는 경우, 이 단어는 흔하게 등장하는 것을 의미하는 데, 이것을 단어가 나타난 문서의 수 DF(Documnet Frequency, 문서 빈도)라고 하며, IDF는 이 값의 역수를 의미합니다.
# 
# 
# * TF-IDF 값은 특정 단어의 상대적인 빈도수를 나타내 주는 값이다. 값이 클 수록 현재 문서에서는 자주 언급되면서 다른 문서에서는 잘 언급되지 않음을 뜻하고, 값이 작을수록 다른 문서에는 자주 언급되면서 현재 문서와 관련성이 낮음을 의미합니다.
# 
# 
# * 핵심어는 특정 문서에서 특정 단어가 많이 등장하는 어휘빈도(TF)와 다른 문서에서 등장하지 않는 문서 역빈도(IDF)의 곱을 통해 추출합니다.

# In[24]:


# 특징 추출 방법으로 TF-IDF 값을 사용할 경우, 단순 횟수를 이용하는 것보다 각 단어의 특성을 좀 더 잘 반영함으로 
# Countvectorizer보다 더 좋은 결과를 만들어낼 수 있습니다.

# TF-IDF를 구하기 위해서는 TfidfVectorizer 라이브러리를 설치해야 합니다.

from sklearn.feature_extraction.text import TfidfVectorizer

# TfidfVectorizer() 통해 문서 내에서 특정 단어의 중요도를 구하겠습니다.
# 빈도가 높은 300개의 단어의 벡터화를 진행하겠습니다.
travel_tfidv = TfidfVectorizer().fit(travel_top_nouns)

# 추출한 명사가 블로그 내용에서 어떤 TF-IDF 값을 가지는지 배열 형태로 출력하겠습니다.
print(travel_tfidv.transform(contents).toarray())
print(travel_tfidv)


# In[25]:


# 단어사전을 출력하겠습니다.
word_tfidv = travel_tfidv.vocabulary_

# TF-IDF 값을 DataFrame 형식으로 만들겠습니다.
df_tfidv = pd.DataFrame(travel_tfidv.transform(contents).toarray())

# 각 단어에 부여된 인덱스를 기준으로 정렬해서 단어사전을 출력하겠습니다.
print(sorted(word_tfidv.items()))
df_tfidv


# **현재, 행렬에서는 컬럼이 숫자로 출력되어 숫자가 의미하는 단어를 알기 어렵습니다. 아래에서 숫자를 단어로 변환하는 과정을 수행하겠습니다.**

# In[26]:


# df_tfidv 행렬의 컬럼을 숫자에서 추출한 단어로 변환시키겠습니다.
# 먼저, 컬럼에 매칭시킬 단어 리스트를 만들기 위해 (단어, 인덱스) 의 튜플형식에서 단어부분을 가져오겠습니다.

sort_word = sorted(word_tfidv.items())

sort_word_list = []
for i in sort_word:
    sort_word_list.append(i[0])

print(len(sort_word_list))  # 한 글자 단어를 제외한 총 261개의 단어가 리스트로 만들어졌습니다.
sort_word_list[:10] # 단어가 리스트 형태로 출력되었습니다.


# In[27]:


# 저장된 단어 리스트를 컬럼으로 입력하겠습니다.

df_tfidv.columns = sort_word_list

df_tfidv


# **행렬에서 컬럼이 숫자에서 단어로 변환되어 출력되었습니다. BoW 와 같이 각 단어별 총 TF-IDF 산출하겠습니다.**

# In[28]:


# 먼저 df_tfidv 의 컬럼을 리스트로 만들겠습니다.
df_tfidv_col_list = list(df_tfidv.columns)

# 만든 리스트를 enumerate() 함수를 활용하여 딕셔너리 형태로 만들겠습니다.
df_tfidv_col_dict = {index : word for word, index in enumerate(df_tfidv_col_list)}

# df_tfidv_col_dict 의 values 부분을 TF-IDF 총합으로 채워넣겠습니다.
for word, idx in df_tfidv_col_dict.items():
    total = df_tfidv[word].sum()
    df_tfidv_col_dict[word] = total

print(df_tfidv_col_dict)

# 만들어진 {단어 : TF-IDF} 을 DataFrame 으로 변환하고, 그것을 Transpose 하겠습니다.
tfidf_dict_df = pd.DataFrame([df_tfidv_col_dict]).T

# 컬럼이름을 TF-IDF 로 변경하겠습니다.
tfidf_dict_df.columns = ['TF-IDF']

# 만들어진 딕셔너리와 함께 DataFrame(내림차순 정렬) 을 출력하겠습니다.
sorted_tfidf_dict_df = tfidf_dict_df.sort_values(by = 'TF-IDF', ascending = False)

sorted_tfidf_dict_df.head(20)


# **TF-IDF 별로 살펴보면, 혼자(178.972)가 가장 중요한 단어로 나타났습니다. 다음으로, 여행(161.106), 사진(91.873), 국내(69.72) 등의 순으로 나타났습니다. BOW 결과와 비교하면, 전체적으로 상위에 출력된 단어들은 유사했지만, 세부적인 순위에서는 차이를 보였습니다.**
# 
# 
# **TF-IDF 에서는 제주도(39.373), 강원도(34.765), 경주(33.316), 서울(28.482), 부산(28.018), 여수(24.726) 등의 지역의 중요도가 높은 것으로 나타났습니다.**
# 
# **수집과정에서 입력한 검색어를 제외하면, 사진, 추천, 시간, 바다 등의 단어가 빈도도 높고 중요도도 높은 것으로 나타났습니다.**

# # 4. 사회연결망분석(SNA)

# * 사회연결망 분석(소셜네트워크 분석) : 분석 대상(node)들의 관계(edge)를 연결망(network) 구조로 표현하고 이를 계량적으로 제시하는 분석기법
# 
# 
# * 본 프로젝트에서는 빈도가 높은 300개의 단어(node)들 간의 어떠한 관계(edge)를 네트워크 지도로 살펴보겠습니다.

# In[29]:


import networkx as nx


# In[30]:


travel_sentences = []
for content in contents:
    travel_sentences.extend(re.split(';|\.|\?|\!', content)) # 블로그 내용에 대해서 문장으로 나누기 위해서 문장의 끝을 나타내는 
                                                             # ;,.,?,! 를 구분자로 사용하겠습니다.
travel_sentences[:10]


# In[31]:


# 블로그 내용을 문장별로 구분하고, 구분된 문장 별로 명사를 추출하여 정리하겠습니다

travel_sentence_nouns = []
for sentence in travel_sentences:
    sentence_nouns = mecab.nouns(sentence)
    if sentence_nouns not in stop_words:
        travel_sentence_nouns.append(sentence_nouns)

travel_sentence_nouns[0:5]


# In[32]:


# 상위 단어 top_nouns 에 대해서 key에 해당하는 단어, value에 해당하는 id를 넣어 딕셔너리 형태로 저장하겠습니다.

travel_word2id = {word: num for num, word in enumerate(sorted_tfidf_dict_df.index)}
sorted(travel_word2id.items(), key=lambda x: x[1], reverse=False)[:10]


# In[33]:


# 상위 단어 top_nouns 에 대해서 key에 해당하는 id, value에 해당하는 단어를 넣어 딕셔너리 형태로 저장하겠습니다.

travel_id2word = {num: word for num, word in enumerate(sorted_tfidf_dict_df.index)}
sorted(travel_id2word.items(), key=lambda x: x[1], reverse=False)[:10]


# In[34]:


# 상위 단어들에 대해서 그 개수만큼의 인접 행렬을 만들고, 문장 내에 상위 단어가 함께 포함된 비중에 따라 가중치를 계산하겠습니다.
# 행렬에서 가중치가 0 이상이면 서로 연결되어 있음을 의미합니다.

travel_adjacent_matrix = np.zeros((len(travel_word2id), len(travel_word2id)), int)
for sentence in travel_sentence_nouns:
    for wi, i in travel_word2id.items():
        if wi in sentence:
            for wj, j in travel_word2id.items():
                if i != j and wj in sentence:
                    travel_adjacent_matrix[i][j] += 1
travel_adjacent_matrix


# In[35]:


# 인접 행렬로 연결망을 만들겠습니다.

travel_network = nx.from_numpy_matrix(travel_adjacent_matrix)
list(travel_network.adjacency())[0]


# ## 4.1 연결 중심성
# 
# * 특정 단어에 직접 연결된 다른 단어의 수가 많으면 연결 중심성이 높다고 해석합니다.

# In[36]:


# id에 대응되는 단어 컬럼을 생성하고 테이블을 만드는 함수를 생성하겠습니다.
def create_df(x):
    word_list = []
    for i in x['id']:
        word_list.append(travel_id2word.get(i))
    x['word'] = word_list
    return x


# In[37]:


# 네트워크를 만들고 중심성별로 내림차순 정렬하겠습니다.
deg = nx.degree_centrality(travel_network)
sorted_deg = sorted(deg.items(), key = lambda x: x[1], reverse=True)

# 데이터프레임으로 만들겠습니다.
df_sorted_deg = pd.DataFrame(sorted_deg)
df_sorted_deg.columns = ['id', 'deg_cent']

# word 추가 함수 적용
df_sorted_deg = create_df(df_sorted_deg)
df_sorted_deg


# ## 4.2 위세 중심성
# 
# * 연결된 상대 단어의 중요성에 가중치를 두어 중요한 단어(연결 중심성이 높은 다른 단어)와 많이 연결될수록 위세 중심성이 높다고 해석합니다.

# In[38]:


# 네트워크를 만들고 중심성별로 내림차순 정렬하겠습니다.
eig = nx.eigenvector_centrality(travel_network, weight='weight')
sorted_eig = sorted(eig.items(), key = lambda x: x[1], reverse=True)

# 데이터프레임으로 만들겠습니다.
df_sorted_eig = pd.DataFrame(sorted_eig)
df_sorted_eig.columns = ['id', 'eigen_cent']
df_sorted_eig  # 출력하면 id에 매핑된 단어가 포함되지 않아 id에 해당하는 단어를 추가하겠습니다.

# word 추가 함수 적용
df_sorted_eig = create_df(df_sorted_eig)
df_sorted_eig


# ## 4.3 근접 중심성
# 
# * 직간접적으로 연결된 다른 모든 단어간의 거리를 계산하여 전체 연결망의 중심적 위치에서 다른 단어들과 가까운 위치에 위치하고 있다면, 근접 중심성이 높다고 해석합니다.

# In[39]:


# 네트워크를 만들고 중심성별로 내림차순 정렬하겠습니다.
clo = nx.closeness_centrality(travel_network, distance='weight')
sorted_clo = sorted(clo.items(), key = lambda x: x[1], reverse=True)

# 데이터프레임으로 만들겠습니다.
df_sorted_clo = pd.DataFrame(sorted_clo)
df_sorted_clo.columns = ['id', 'closure_cent']
df_sorted_clo  # 출력하면 id에 매핑된 단어가 포함되지 않아 id에 해당하는 단어를 추가하겠습니다.

# word 추가 함수 적용
df_sorted_clo = create_df(df_sorted_clo)
df_sorted_clo


# ## 4.4 매개 중심성
# 
# * 다른 단어들 사이에 얼마나 매개자 역할을 수행하는가에 가중치를 두는 것으로 매개역할을 많을수록 매개 중심성이 높다고 해석합니다.

# In[40]:


# 네트워크를 만들고 중심성별로 내림차순 정렬하겠습니다.
betw = nx.current_flow_betweenness_centrality(travel_network)
sorted_betw = sorted(betw.items(), key = lambda x: x[1], reverse=True)

# 데이터프레임으로 만들겠습니다.
df_sorted_betw = pd.DataFrame(sorted_betw)
df_sorted_betw.columns = ['id', 'between_cent']
df_sorted_betw  # 출력하면 id에 매핑된 단어가 포함되지 않아 id에 해당하는 단어를 추가하겠습니다.

# word 추가 함수 적용
df_sorted_betw = create_df(df_sorted_betw)
df_sorted_betw


# ## 4.5 중심성(종합)

# In[41]:


# 각 중심성별로 상위 10개의 단어와 중심성 지수를 정리했습니다.

total_word = pd.DataFrame(df_sorted_eig[['word', 'eigen_cent']])
total_word['연결중심성_word'] = df_sorted_deg['word']
total_word['연결중심성_cent'] = df_sorted_deg['deg_cent']

total_word['근접중심성_word'] = df_sorted_clo['word']
total_word['근접중심성_cent'] = df_sorted_clo['closure_cent']

total_word['매개중심성_word'] = df_sorted_betw['word']
total_word['매개중심성_cent'] = df_sorted_betw['between_cent']
total_word.columns = ['위세_단어', '위세중심성', '연결_단어', '연결중심성', '근접_단어','근접중심성', '매개_단어','매개중심성']
total_word.head(15)


# **1. 각 중심성별로 상위 10개의 단어를 살펴보면, 국내, 여행, 시간, 사진, 사람, 추천, 생각 등이 각 중심성에서 공통적으로 중요도가 높은 것으로 나타났습니다.**
# 
# **2. 위세 중심성을 살펴보면, 강원도, 서울, 제주도 등의 지역 관련 단어가 다른 중심성에 비해 중요도가 높게 나타났습니다.**
# 
# **3. 매개 중심성을 살펴보면, 다른 중심성에 비해 값이 작은 것으로 보아 단어 간의 직접 연결이 많다는 것을 알 수 있습니다.**

# In[42]:


# 각 중심성별로 상위 10개의 단어를 시각화하겠습니다.

fig, ax = plt.subplots(2,2, figsize = (15,10))

sns.barplot(data = df_sorted_eig.head(10), x = 'word', y= 'eigen_cent', ax = ax[0][0])
sns.barplot(data = df_sorted_deg.head(10), x = 'word', y= 'deg_cent', ax = ax[0][1])
sns.barplot(data = df_sorted_clo.head(10), x = 'word', y= 'closure_cent', ax = ax[1][0])
sns.barplot(data = df_sorted_betw.head(10), x = 'word', y= 'between_cent', ax = ax[1][1])

ax[0][0].set_title('위세 중심성')
ax[0][1].set_title('연결 중심성')
ax[1][0].set_title('근접 중심성')
ax[1][1].set_title('매개 중심성')
plt.subplots_adjust(hspace = 0.3)


# ## 4.6 네트워크 그림
# 
# * networkx에서 기본적으로 제공하는 시각화 레이아웃 중 spring layout을 사용하겠습니다.
# 
# 
# * node size는 위세 중심성을 기초로 설정했습니다.

# In[43]:


# 생성된 연결망 데이터를 시각화하겠습니다.

import matplotlib.pyplot as plt

plt.figure(figsize=(50, 40))

nx.draw_spring(travel_network, labels = travel_id2word, font_family = 'Malgun Gothic', font_color='blue',
               node_color = ['yellow'], node_size = [v * 20000 for _,v in list(sorted_eig)], font_size=25, font_weight='bold',
              edge_color = '#D4D5CE')
plt.title('Spring Layout', fontsize = 50)


# * 위세 중심성은 연결된 단어의 연결성까지도 계산함으로 연결된 단어가 다른 단어와 연결성이 높다면, 해당 단어의 위세 중심성은 높다고 판단하는 중심성이며, 즉 영향력이 높은지를 측정합니다.
# 
# 
# * 결과는 아래와 같습니다.
# 
# 
#     - 네트워크 지도에서 노드 크기가 큰 단어를 살펴보면, 여행, 국내, 혼자, 추천, 사진, 제주도(제주), 시간, 카페 등으로 나타났으며, 네트워크 상에서 중심부에 위치하고 있습니다.
# 
#     - 네트워크 지도에 포함된 지역을 살펴보면, 제주, 강원도(강릉, 춘천, 속초, 평창-대관령, 동해), 부산(해운대), 인천, 태안, 군산, 여수, 울산, 통영, 포항 등 바닷가 인접 지역이 많이 포함되었습니다. 이외, 대구, 서울, 순천, 경주, 전주(한옥마을), 단양, 제천, 대전 등 대도시를 포함한 다양한 도시들도 포함되었습니다. 결과를 종합하면, '바다'라는 키워드를 중심으로 사람들은 항구도시를 여행지로 선호하는 것으로 보였으며, 그 외 대구, 서울, 경주, 전주 등 대도시 및 옛 전통이 깊은 도시도 많은 사람이 찾는 것으로 보여집니다.
# 
#     - 여행에서의 계획을 짤 때 고려하는 사항은 맛집, 카페, 숙소, 거리, 계절, 날씨 등의 중요도가 높은 것으로 나타났으며, 그 중에서도 맛집, 카페 등 먹거리에 대한 관심이 높은 것으로 보여졌습니다.

# ## 4.7 커뮤니티 탐지
# 
# * 위의 네트워크 지도에서는 커뮤니티를 찾기 힘듭니다. 아래에서 단어들 간의 커뮤니티를 찾아 그래프로 출력해보겠습니다.
# 
# * 커뮤니티를 찾기 위해 Louvain 알고리즘을 사용하겠습니다. 이 알고리즘은 다른 알고리즘과는 달리 계산 시간이 빠르다는 장점으로 많이 이용되고 있습니다.

# In[44]:


# 커뮤니티를 찾기 위한 modularity 를 계산하겠습니다.

from community import community_louvain

# 노드 속성을 기초로 파티션을 나누겠습니다.
partition = community_louvain.best_partition(travel_network)

# partition 값을 통해 노드가 잘 구분되어 있는지를 계산하겠습니다.
modularity = community_louvain.modularity(partition, travel_network)
print('Modularity:', modularity)


# In[45]:


plt.figure(figsize=(25, 20))

colors = [partition[n] for n in travel_network.nodes()]
my_colors = plt.cm.Set3_r
nx.draw(travel_network, with_labels = True, labels = travel_id2word, font_family = 'Malgun Gothic', 
        node_color=colors, cmap = my_colors, font_size = 14, edge_color = "#D4D5CE")


# **커뮤니티 탐지 결과, 5개의 커뮤니티로 나누어졌습니다. 각 커뮤니티의 노드 색상은 노랑, 하늘, 회색, 보라, 분홍색으로 출력되었습니다.**
# 
# **현재 생성된 커뮤니티 갯수가 최적인지를 확인하기 위해 아래에서 엘보우 기법을 활용하겠습니다.**

# In[46]:


from sklearn.cluster import KMeans  
from gensim.models import Word2Vec  # 언어의 의미와 유사도를 고려하여 언어를 벡터로 매핑하는 방식을 사용하는 패키지
from sklearn.manifold import TSNE   # t-SNE는 원본 데이터를 가장 잘 표현할 수 있도록 데이터의 차원을 줄이는 알고리즘


# In[47]:


# 데이터

travel_nouns = [list(vocab_dict.keys())]

travel_nouns[0][:10]


# In[48]:


# 단어 임베딩을 실시하여 벡터를 구하겠습니다.

travel_word2vec = Word2Vec(travel_nouns, min_count= 1)


# In[49]:


# 단어벡터에 대한 유사도를 구하겠습니다.
travel_vocab = travel_word2vec.wv.vocab
travel_similarity = travel_word2vec[travel_vocab]


# In[50]:


# TSNE 라이브러리를 활용하여 특징 선택 방법을 통한 차원 축소를 실시하겠습니다.

travel_tsne = TSNE(n_components=2)  # n_components=2 == 2차원으로 변환하겠습니다.


# In[51]:


# 위에서 차원축소한 데이터를 학습시키고 변환시키겠습니다(fit_transform()메서드).

travel_transform_similarity = travel_tsne.fit_transform(travel_similarity)
travel_df = pd.DataFrame(travel_transform_similarity, index = travel_vocab, columns=['x', 'y'])

travel_df.head()


# * K-means 클러스터링은 비지도 학습 알고리즘으로서 클러스터 내 오차제곱합(SSE)의 값이 최소가 되도록 클러스터의 중심을 결정해나가는 방법입니다. elbow 방법은 클러스터 개수에 따른 데이터의 SSE값을 그래프로 그려 최적의 클러스터 개수를 발견하는 방법입니다.

# In[52]:


# 엘보우 기법을 통해 적절한 클러스터 개수를 구하겠습니다.

def elbow(x):
    distortions  = []
    for i in range(1,20):
        km = KMeans(n_clusters = i, init='k-means++', random_state = 33)
        km.fit(x)
        distortions.append(km.inertia_)  # inertia_ : kmeans 클러스터링으로 계산된 SSE 값
    
    plt.plot(range(1,20), distortions, marker='o')
    plt.plot([6,6],[6,13000], ':')
    ticks = plt.xticks(range(len(distortions)+1))
    plt.xlabel('클러스터 갯수')
    plt.ylabel('SSE')
    plt.show()
    
elbow(travel_df)


# **엘보우 기법을 통해 최적의 클러스터 개수는 6에서 기울기가 작아지는 것을 확인했습니다. 아래에서 클러스터의 수를 6으로 설정하여 군집분석을 수행하겠습니다.**

# # 5. 군집분석

# * 위에서 찾은 클러스터 개수를 활용하여 군집분석을 하기 위해 k-means 알고리즘을 사용하겠습니다.
# 
# 
# * 군집분석은 데이터의 어떤 영역을 대표하는 클러스터 중심을 찾습니다. 먼저, 데이터 포인트를 가장 가까운 클러스터 중심에 할당하고, 그런 다음 클러스터에 할당된 데이터 포인트의 평균으로 클러스터 중심을 다시 지정하는 단계를 거치는 방법입니다.

# In[53]:


# 엘보우 기법으로 찾은 클러스터 갯수로 군집분석을 실시하겠습니다.

travel_kmeans = KMeans(n_clusters = 6)
travel_predict = travel_kmeans.fit_predict(travel_df)
travel_predict


# In[54]:


travel_results = travel_df
travel_results['cluster'] = travel_predict
travel_results


# In[55]:


# 클러스터별(0~5)로 묶인 단어 20개를 출력하는 함수를 만들겠습니다.
# 0번 클러스터에 속한 단어를 확인하겠습니다.

def cluster_output(data, cluster):
    return data[data['cluster'] == cluster]

cluster_output(travel_results, 0).head(20)


# * 새로이 커뮤니티 탐지를 수행하기 위해 각 단어와 클러스터 숫자를 매핑한 딕셔너리를 만들겠습니다.

# In[56]:


# 각 클러스터에 포함된 단어를 저장하겠습니다.

zero_cluster = cluster_output(travel_results, 0).index
one_cluster = cluster_output(travel_results, 1).index
two_cluster = cluster_output(travel_results, 2).index
three_cluster = cluster_output(travel_results, 3).index
four_cluster = cluster_output(travel_results, 4).index
five_cluster = cluster_output(travel_results, 5).index


# In[57]:


# 원본 딕셔너리를 travel_word2id 정보가 훼손될 수 있으므로 복사본인 새로운 딕셔너리를 만들겠습니다.

travel_word2id_cluster6 = travel_word2id.copy()


# In[58]:


# For 문을 통해 각 클러스터에 포함된 단어와 travel_word2id_cluster6의 키 값이 일치하면 클러스터 숫자를 value 값으로 넣겠습니다. 

for word, idx in travel_word2id_cluster6.items():
    for zero in list(zero_cluster):
        if zero == word:
            travel_word2id_cluster6[word] = 0
    
    for one in list(one_cluster):
        if one == word:
            travel_word2id_cluster6[word] = 1
            
    for two in list(two_cluster):
        if two == word:
            travel_word2id_cluster6[word] = 2
            
    for three in list(three_cluster):
        if three == word:
            travel_word2id_cluster6[word] = 3
            
    for four in list(four_cluster):
        if four == word:
            travel_word2id_cluster6[word] = 4        
            
    for five in list(five_cluster):
        if five == word:
            travel_word2id_cluster6[word] = 5

print(len(travel_word2id_cluster6))
sorted(travel_word2id_cluster6.items(), key=lambda x: x[0], reverse=False)[:10]


# In[59]:


# key 에 저장된 단어를 숫자로 변환하기 위해 enumerate() 함수를 사용하겠습니다.
new_travel_word2id_cluster6 = {}
for key, value in enumerate(travel_word2id_cluster6.values()):
    new_travel_word2id_cluster6[key] = value

print(len(new_travel_word2id_cluster6))
sorted(new_travel_word2id_cluster6.items(), key=lambda x: x[0], reverse=False)[:10]


# **변환된 딕셔너리 결과는 위의 결과와 일치하는 것을 확인할 수 있습니다.**

# In[60]:


# 군집분석 결과를 시각화하겠습니다.

plt.figure(figsize = (12, 8))
plt.rc('axes', unicode_minus = False)
sns.scatterplot(x = 'x', y = 'y', data = travel_results, hue = 'cluster', palette='deep')
plt.legend(loc = 'best')


# **아래에서 커뮤니티를 출력하겠습니다.**

# In[61]:


plt.figure(figsize=(25, 20))

colors = [new_travel_word2id_cluster6[n] for n in travel_network.nodes()]
my_colors = plt.cm.Set2_r
nx.draw(travel_network, with_labels = True, labels = travel_id2word, font_family = 'Malgun Gothic', 
        node_color=colors, cmap = my_colors, font_size = 14, edge_color = '#D4D5CE', font_weight='bold')


# **클러스터 갯수에 맞게 각 클러스터별로 연두, 분홍, 파랑, 주황, 베이지, 회색으로 출력되었습니다.**

# **각 단어별 x, y좌표에 위치한 단어를 그래프로 출력하겠습니다.**

# In[62]:


travel_tsne = TSNE(n_components=2)
travel_transform_similarity = travel_tsne.fit_transform(travel_similarity)
travel_df = pd.DataFrame(travel_transform_similarity, index = travel_vocab, columns=['x', 'y'])

travel_df.head()


# In[63]:


plt.figure(figsize = (40, 20))
ax = sns.scatterplot(travel_df["x"], travel_df["y"])

for word, pos in travel_df.iterrows():
    ax.annotate(word, pos)
plt.show()


# # 6. 유사도

# ## 6.1 문서 간 유사도

# In[64]:


# TF-IDF 값을 활용하여 문서 간 코사인 유사도를 구하겠습니다.

from sklearn.metrics.pairwise import linear_kernel  # linear_kernel는 두 벡터의 dot product 를 계산해주는 라이브러리입니다.

cosine_sim = linear_kernel(df_tfidv)

cosine_sim_df = pd.DataFrame(cosine_sim)

cosine_sim_df


# In[65]:


# 가장 유사한 문서를 찾는 함수를 만들겠습니다.

def most_similar(x, index):
    x = x.loc[index].sort_values(ascending = False).head(2)
    df = pd.DataFrame(x)
    df.columns = ['유사도']

    return df.tail(1)

most_similar(cosine_sim_df, 1)


# **예시로, 1번 문서와 가장 유사한 문서는 619번 문서이고 유사도는 0.857 으로 나타났습니다.**

# ## 6.2 단어 간 유사도

# In[66]:


# 데이터

dataset = []
for i in han_contents:
    dataset.append(mecab.nouns(i))
dataset = [[y for y in x if len(y) >= 2] for x in dataset]
dataset = [[y for y in x if y not in stop_words] for x in dataset]

dataset[0][:5]


# * Word2Vec(data = data, size = 벡터의 차원, window = 주변단어 범위, min_count = 최소 빈도 설정, workers = 실행할 병렬 프로세스의 수, sg = 단어 예측방식(0 == CBOW, 1 == skip-gram))

# In[67]:


# Word2Vec을 통해 단어 임베딩을 수행하겠습니다.
model = Word2Vec(dataset, window = 5, min_count= 2, sg = 1)
model.init_sims(replace = True)  # init_sims() : 트레이닝이 완료되면 필요없는 메모리를 unload 시킵니다.


# In[68]:


print(f"대구와 부산 두 단어 간 유사도 : {model.wv.similarity('대구', '부산')}")


# In[69]:


# 유사도를 테이블로 출력하는 함수를 만들겠습니다.
def sim_table(x):
    return pd.DataFrame(model.wv.most_similar(x, topn = 100), columns = ['단어', '유사도'])

df = sim_table('해변')
df.head(10)


# In[70]:


# 임의로 전국 20개 여행지역을 리스트로 저장하고, '해변' 유사어 중 포함여부를 측정해 봤습니다.

city_list = ['제주', '속초', '강릉', '속초', '평창', '동해', '부산', '인천', '태안', '군산', '여수','울산', '통영', '포함', 
             '대구', '서울', '순천', '경주', '전주', '단양']
df = df[df['단어'].isin(city_list)]
df


# **전국 여행지역 20곳을 기준으로 공통되는 키워드를 찾았으나 '해변'이라는 키워드에서만 동해와 강릉이 출력되었습니다. 예측과는 달리 혼행족이 많이 다니는 여행지 간의 공통적인 요소를 찾기 힘들었습니다. 각 여행지마다 고유의 특색이 있는 세부적인 지명과 음식 이름 등이 많이 출력되었습니다.**

# # 7. 추천 시스템

# * 추천 시스템을 개발하기 위해서는 label(지역이름) 값이 있어야 합니다. 지역이름을 추출하기 위해 다음과 같은 과정을 수행했습니다.
# 
# 
#     - 먼저, 전국의 도(ex. 경기도, 경상북도 등) 리스트와 지역(예, 서울, 부산 등) 리스트를 만들어줍니다.
#     
#     - 기존 컬럼 중 'Title'과 'Description' 을 합쳐 새로운 컬럼 'txt_sum' 을 만듭니다.
# 
#     - 마지막으로 반복문을 통해 'txt_sum' 컬럼에 도 및 지역 리스트가 포함되는지를 통해 해당 블로그 글이 소개하는 지역을 추출했습니다.

# In[71]:


city_data = pd.read_csv('etc/korea_city_list.csv')

do_list = list(set(city_data['do'].str.strip()))[1:10]
city_list = list(set(city_data['city'].str.strip()))

data['txt_sum'] = data['Title'] + data['Description']

def find_city_name():
    do_result = []
    city_result = []

    for txt in data['txt_sum']:
        do_match = []
        city_match = []

        for target in do_list:
            search_result = str(txt).find(str(target))
            if search_result != -1:
                do_match.append(target)
#                 print(target)

        for target in city_list:
            search_result = str(txt).find(str(target))
            if search_result != -1:
                city_match.append(target)
#                 print(target)

        do_result.append(','.join(do_match))
        city_result.append(','.join(city_match))

    return do_result, city_result

do_result, city_result = find_city_name()

data['do'] = do_result
data['city'] = city_result

data[data['do'] != '']
data[data['city']!= '']

data.to_csv('first_area_name.csv', encoding = 'utf8')


# * 생성된 지역 컬럼을 출력해보겠습니다.

# In[72]:


data = pd.read_csv('first_area_name.csv')

print(data.shape)
data.head()


# * 성공적으로 추출되었음을 확인했습니다. 이제 지역명이 도 혹은 지역컬럼이 채워진 데이터 갯수를 살펴보겠습니다.

# In[73]:


data_notnull = data.loc[data['do'].notnull() | data['city'].notnull()]

print(data_notnull.shape)
data_notnull.tail()


# * 지역명이 채워진 데이터의 총 갯수는 810개입니다. 하지만, 지역명이 두 개이상으로 채워진 케이스가 보여 확인해보겠습니다.

# In[74]:


data['do'].value_counts()


# In[75]:


data['city'].value_counts()


# In[76]:


data['city'].unique()


# 지역이 두 개이상으로 채워진 데이터 갯수를 확인했습니다. 지역이 두 개이상 채워진 케이스는 직접 블로그 내용을 비교하며 단일 지역명으로 수정하겠습니다. 또한, 여행글과 관련없거나 여러 지역이 포함된 케이스는 지우겠습니다.
# 
# 
# 수정된 지역컬럼은 다음과 같습니다.

# In[77]:


area = pd.read_csv('area_name.csv')

area_notnull = area.loc[area['do'].notnull() | area['city'].notnull()]

print(area_notnull.shape)

area_notnull.head()


# * 위의 행렬에서 인덱스가 정리되지 않았습니다. reset_index() 를 활용하여 인덱스를 정리하겠습니다.

# In[78]:


area_notnull = area_notnull.reset_index()

area_notnull.head()


# * 기존의 인덱스를 삭제하겠습니다.

# In[79]:


area_notnull = area_notnull.drop(['index', 'Unnamed: 0'], axis = 1)

area_notnull.head()


# * 위에서 했던 중복값 체크를 다시 하겠습니다.

# In[80]:


print('원본 포스팅 글 수 :',area_notnull.shape)

area_notnull = area_notnull.drop_duplicates(['Post_Contents'], keep = 'last') # 가장 최근 내용을 남기겠습니다.

print('중복 제거 후 포스팅 글 수 :', area_notnull.shape)


# * 지역이 두 개이상으로 된 케이스 유무를 확인하겠습니다.

# In[81]:


area_notnull['do'].unique()


# In[82]:


sns.countplot(data = area_notnull, x = 'do')


# **시각화 결과, 도 단위 중에서는 제주도와 강원도를 가장 많이 방문하는 것으로 나타났습니다.**

# In[83]:


area_notnull['city'].unique()


# In[84]:


popular_area = area_notnull['city'].value_counts().head(10).index  # 도시 중 가장 빈도가 높은 10개

popular_city = area_notnull[area_notnull['city'].isin(popular_area)]  # 상위 10개 도시의 데이터 추출

sns.countplot(data = popular_city, x = 'city')  # 시각화


# **빈도가 높은 상위 10개의 지역을 시각화한 결과, 제주를 가장 많이 여행하는 것으로 나타났습니다. 다음으로 경주, 부산 등의 순이었습니다.**

# * 단일 지역으로 변경되었음을 확인했습니다. 이후, 'do' 컬럼과 'city' 컬럼을 합쳐 'area' 컬럼을 생성하겠습니다. 이때, 두 컬럼 모두 값이 채워졌을 경우에는 city 컬럼 데이터가 보다 구체적인 지역명이므로 이를 사용하겠습니다.

# In[85]:


area_notnull['area'] = area_notnull['city']
area_notnull.loc[area_notnull['area'].isnull(), 'area'] = area_notnull['do']


# In[86]:


print('결측치 수 : ',area_notnull['area'].isnull().sum())

print('최종 데이터 수 :', area_notnull.shape)
area_notnull['area'].head()


# * area 컬럼을 모두 정리했습니다. 총 734개 데이터를 활용하여 여행지 추천시스템을 구현하겠습니다.

# * 추천시스템 구현을 위해 feature은 Post_Contets 컬럼이며, label은 area 컬럼을 활용하겠습니다. 먼저, Post_Contents 컬럼을 개행문자 제거와 정규표현식을 이용하여 한글을 제외하고 모두 제거하겠습니다.

# In[87]:


# 'Post_Contents' 를 한글을 제외한 모든 문자를 제거하하겠습니다.

def revised_text(data):
    
    contents = []
    posts = data['Post_Contents']
    for post in posts:
        post = str(post).replace('\n','').replace('\u200b','').replace('\xa0','').replace('\t','')
        post = re.sub('[^ㄱ-ㅎㅏ-ㅣ가-힣 ]',' ',post).lstrip()
        contents.append(str(post))
    return contents

area_notnull['reviesed_contents']  = revised_text(area_notnull)


# In[88]:


area_notnull.head()


# * 성공적으로 데이터가 변환되었습니다. 이제부터 TFIDF를 통해 코사인 유사도를 계산하여 추천시스템을 구현하겠습니다.

# In[89]:


from sklearn.feature_extraction.text import TfidfVectorizer

tfidf = TfidfVectorizer(stop_words = stop_words)

# 네트워크 분석 과정과는 달리 입력 형식이 다양하기 때문에 품사에 구분없이 모두 벡터화했습니다.
tfidf_matrix = tfidf.fit_transform(area_notnull['reviesed_contents'])

print(tfidf_matrix.shape)


# **총 734개의 문서의 텍스트를 벡터화한 결과 114450개로 나타났습니다.**

# In[90]:


from sklearn.metrics.pairwise import linear_kernel

cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)  # 코사인 유사도 계산


# In[91]:


print(tfidf.transform(area_notnull['reviesed_contents']).toarray())
print(tfidf)


# In[92]:


df_tfidv = pd.DataFrame(tfidf.transform(area_notnull['reviesed_contents']).toarray())

df_tfidv # 문서(블로그) * 단어


# In[93]:


# 인덱스를 지역이름으로 저장하겠습니다.
area_list = list(area_notnull['area'].values)

df_tfidv.index = area_list

df_tfidv


# In[94]:


word_tfidv = tfidf.vocabulary_   # 벡터 단어 출력

sort_word = sorted(word_tfidv.items())

sort_word_list = []
for i in sort_word:
    sort_word_list.append(i[0])

print(len(sort_word_list))  # 한 글자 단어를 제외한 총 261개의 단어가 리스트로 만들어졌습니다.
sort_word_list[:10]


# In[95]:


# 벡터 단어를 컬럼으로 저장하겠습니다.
df_tfidv.columns = sort_word_list

df_tfidv


# ## 7.1 아이템 기반 여행지 추천

# * 위에서 만들어진 여행지역이름 * 벡터화된 던어의 코사인 유사도 행렬을 통해 추천시스템 함수를 구현하겠습니다.
# 
# 
# * 아이템 기반 여행지 추천시스템은 품사 관계없이 학습된 데이터 내에 포함된 범위 내에서 특정 단어를 입력하면 유사도가 높은 특정 지역을 추천해주는 구조을 가지고 있습니다.
# 
# 
# * 예를 들어, '바다'를 검색하면, '바다'와 유사도가 높은 상위 5개의 지역을 추천해줍니다.

# In[96]:


def item_to_area_recommend(keyword):
    sorted_result = df_tfidv[keyword].sort_values(ascending = False).head()
    area_list = []
    dict_result = {}
    for area, sim in sorted_result.items():
        area_list.append(area)
        if area_list.count(area) == 1:
            dict_result[area] = sim
        else:
            dict_result[area] = sorted_result.loc[area].mean()
    series_result = pd.Series(dict_result)

    return series_result


# In[97]:


item_to_area_recommend('바다')


# * 위에서 구현한 item_to_area_recommend 함수에 '바다' 라는 키워드를 입력하면 5개의 지역이 출력됩니다.

# ## 7.2 유사 여행지 추천

# * 본 추천시스템은 특정 여행지를 입력하면 유사도가 높은 여행지를 추천해주는 시스템입니다.
# 
# 
# * 예를 들어, '대구' 라고 입력하면, 유사도가 높은 특정 여행지를 추천해줍니다.

# In[98]:


from sklearn.feature_extraction.text import TfidfVectorizer

tfidf = TfidfVectorizer(stop_words = stop_words)
tfidf_matrix = tfidf.fit_transform(area_notnull['reviesed_contents'])

print(tfidf_matrix.shape)


# In[99]:


from sklearn.metrics.pairwise import linear_kernel
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)


# In[100]:


indices = pd.Series(area_notnull.index, index=area_notnull['area']).drop_duplicates()
print(indices.head())


# In[101]:


def area_to_area_recommend(area, cosine_sim=cosine_sim):
    
    # 지역이름으로부터 해당되는 인덱스를 받아옵니다.
    idx = indices[area]

    # 모든 지역에 대해서 해당 지역과의 유사도를 구합니다.
    sim_scores = list(enumerate(cosine_sim[idx]))

    # 유사도에 따라 지역들을 정렬합니다.
    sim_scores = sorted(sim_scores, key=lambda x: x[0], reverse=True)

    # 가장 유사한 10개의 지역을 받아옵니다.
    sim_scores = sim_scores[1:11]

    # 가장 유사한 10개의 지역의 인덱스를 받아옵니다.
    travel_indices = [i[0] for i in sim_scores]

    # 가장 유사한 10개의 지역이름을 리턴합니다.
    similar_area = [] 
    for area in area_notnull['area'].loc[travel_indices].values:
        if area not in similar_area:
            similar_area.append(area)
    
    return pd.Series(similar_area)


# In[102]:


area_to_area_recommend('대구')


# * 위에서 만든 area_to_area_recommend 함수에 '대구' 지역이름을 입력하면 10개의 지역을 추천해줍니다.

# # 8. 종합결과

# ## 8.1 TF-IDF

# In[103]:


tfidf_dict_df.sort_values(by = 'TF-IDF', ascending = False).head(20)


# * TF-IDF는 문서 내에서 특정 단어가 갖는 중요도를 나타내는 가중치입니다. 문서 내에서 특정 단어가 출현하는 빈도와 특정 단어를 갖고 있는
# 문서가 전체 문서에서 차지하는 비율의 역수에 로그를 취한 값을 곱하여 값을 구한다. 이 값이 클수록 중요도가 높다고 간주합니다.
# 
# 
# * TF-IDF 계산 결과, 혼자(179.38)와 여행(161.825)가 가장 중요한 단어라고 나타났습니다. 이는 크롤링 단계에서 검색어에 포함된 단어라는 공통점이 있습니다. 이를 제외한 단어 중에서 살펴보면, 사진(91.949)이 가장 높게 나타났으며, 다음으로 추천(45.24), 제주도(39.494) 등으로 TF-IDF 값이 높았습니다.

# ## 8.2 중심성

# In[104]:


total_word.head(15)


# * 중심성이란 행위자(node)가 네트워크에서 중심에 위치하는 정도를 계량적으로 보여주는 개념입니다. 값이 높을수록 해당 노드는 네트워크 내에서 중요하다고 간주합니다.
# 
# 
# * 네트워크 분석에서 사용된 위세 중심성(노드와 연결된 다른 노드의 영향력을 통해 해당 노드의 중요성을 계산하는 개념)을 살펴보면, TF-IDF 결과와 유사하게 추천(0.173)과 시간(0.136)이 중요한 단어임을 알 수 있습니다. 이외 사진(0.121), 생각(0.12) 등의 순이었습니다. 하지만, 여행, 국내를 제외하면 값이 작아 전체적으로 영향력이 있다고 해석할 수 없습니다. 

# ## 8.3 네트워크 그림

# In[105]:


plt.figure(figsize=(25, 20))

colors = [new_travel_word2id_cluster6[n] for n in travel_network.nodes()]
my_colors = plt.cm.Set2_r

nx.draw(travel_network, with_labels = True, labels = travel_id2word, font_family = 'Malgun Gothic', 
        node_color=colors, cmap = my_colors, font_size = 14, edge_color = '#D4D5CE', font_weight='bold')


# * 각 클러스터에 해당하는 단어는 아래 함수를 통해 출력하겠습니다.

# In[106]:


def cluster_output(data, cluster):
    return data[data['cluster'] == cluster]

print('0번 클러스터')
print(cluster_output(travel_results, 0).head())
print('\n1번 클러스터')
print(cluster_output(travel_results, 1).head())
print('\n2번 클러스터')
print(cluster_output(travel_results, 2).head())
print('\n3번 클러스터')
print(cluster_output(travel_results, 3).head())
print('\n4번 클러스터')
print(cluster_output(travel_results, 4).head())
print('\n5번 클러스터')
print(cluster_output(travel_results, 5).head())


# ## 8.4 단어 간 유사도

# In[107]:


# 두 단어 간 유사도를 구하겠습니다.

def two_word_sim(x, y):
    sim = model.wv.similarity(x, y)
    sim_series = pd.Series(sim)
    df = pd.DataFrame(sim_series)
    df.columns = [y]
    df.index = [x]
    return df

two_word_sim('대구', '막창')


# In[108]:


# 특정 단어와 유사도가 높은 순으로 10개를 출력하겠습니다.

def sim_table(x):
    return pd.DataFrame(model.wv.most_similar(x, topn = 200), columns = ['단어', '유사도'])

df = sim_table('해수욕장')
df.head(10)


# * 임의로 입력한 단어인 해수욕장과 유사한 단어 10개를 출력한 결과입니다.
# 
# 
# * 간략하게 결과를 살펴보면, 하조대, 대천, 변산, 광안리 등 해수욕장 이름이 유사 결과로 출력되었습니다.

# ## 8.5 여행지 추천시스템

# In[109]:


def item_to_area_recommend(keyword):
    sorted_result = df_tfidv[keyword].sort_values(ascending = False).head()
    area_list = []
    dict_result = {}
    for area, sim in sorted_result.items():
        area_list.append(area)
        if area_list.count(area) == 1:
            dict_result[area] = sim
        else:
            dict_result[area] = sorted_result.loc[area].mean()
    series_result = pd.Series(dict_result)

    return series_result


# In[110]:


item_to_area_recommend('바다')


# * 임의로 입력한 단어와 유사도가 높은 지역 5개를 추천되었습니다.

# In[ ]:




