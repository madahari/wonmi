import streamlit as st
import requests
from openai import OpenAI

# OpenAI 클라이언트 초기화
API_KEY = st.secrets["openai"]["api_key"] #openai_api_key
client = OpenAI(api_key  = API_KEY)
# NewsAPI의 API 키 입력
# API_KEY = 'your_news_api_key'  # 발급받은 API 키로 교체

# 뉴스 수집 함수
def fetch_news(keyword):
    url = f"https://newsapi.org/v2/everything?q={keyword}&apiKey={API_KEY}"

    response = requests.get(url)
    if response.status_code == 200:
        return response.json()['articles']
    else:
        return []

# Streamlit 앱 시작
st.title("맞춤형 키워드 뉴스 수집")

# 사용자 입력 받기
keyword = st.text_input("뉴스 키워드를 입력하세요", "주식 AND 상장")

# '뉴스 검색' 버튼이 클릭될 때 뉴스 수집
if st.button("뉴스 검색"):
    with st.spinner("뉴스 수집 중..."):
        # 키워드에 맞는 뉴스 수집
        news = fetch_news(keyword)

    # 수집된 뉴스가 있으면 출력
    if news:
        for article in news:
            st.write(f"### {article['title']}")
            st.write(article['description'])
            st.write(f"[기사 읽기]({article['url']})")
            st.write("---")
    else:
        st.write("해당 키워드에 대한 뉴스를 찾을 수 없습니다.")
