import streamlit as st
from openai import OpenAI

st.title("AI이미지 생성기")
st.write("텍스트를 입력하면, 해당 내용을 바탕으로 이미지를 생성합니다.")

st.sidebar.title("설정")
openai_api_key = st.sidebar.text_input("OpenAI API 키 입력",
                                       type="password")
if not openai_api_key:
    st.sidebar.warning("openAI API키를 입력하세요.")
    st.stop()

client=OpenAI(api_key = openai_api_key)

prompt = st.text_input("이미지 설명을 입력하세요.",
                       value="A cute dog")

# 스타일 버튼 추가
st.write("원하는 스타일을 선택하세요:")
col1, col2, col3 = st.columns(3)
style = ""

with col1:
    if st.button("수채화"):
        style = "watercolor style"
with col2:
    if st.button("픽셀아트"):
        style = "pixel art style"
with col3:
    if st.button("만화"):
        style = "cartoon style"

# 스타일이 선택되면 프롬프트에 추가
if style:
    prompt = f"{prompt}, {style}"

# ...existing code...

if st.button("이미지 생성하기"):
    with st.spinner("이미지를 생성합니다..."):
        try:
            image_urls = []
            for i in range(2):
                response = client.images.generate(
                    prompt = prompt,
                    model = "dall-e-3",
                    n=1,
                    size="1024x1024"
                )
                image_urls.append(response.data[0].url)
            st.image(image_urls, caption=["생성된 이미지 1", "생성된 이미지 2"], use_column_width=True)
        except Exception as e:
            st.error(f"이미지 생성 중 오류가 발생했습니다 :{e}")
# ...existing code...