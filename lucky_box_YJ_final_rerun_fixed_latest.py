
import streamlit as st
import random

st.set_page_config(page_title="어버이날 럭키박스 이벤트", layout="centered")

if "page" not in st.session_state:
    st.session_state.page = 1

prizes = [
    
    "해외여행권 ✈️",
    "명품 시계권 ⌚",
    "박카스 한 병 🧃",
    "신차 인수권 🚗",
    "방울토마토 한 개 🍅",
    "장난감 자동차 🚙",
    "소원권 🙏",
    "뽑기 다시 하기 🔁"
]

def go_to_page(page_number):
    st.session_state.page = page_number
    st.rerun()

# Page 1
if st.session_state.page == 1:
    st.image("./page1.png", use_container_width=True)
    if st.button("다음으로"):
        go_to_page(2)

# Page 2
if st.session_state.page == 2:
    st.subheader("오늘의 경품 라인업 🎁")
    if "shuffled_prizes" not in st.session_state:
        st.session_state.shuffled_prizes = random.sample(prizes, len(prizes))
    for prize in st.session_state.shuffled_prizes:
        st.markdown(f"<h3>{prize}</h3>", unsafe_allow_html=True)
    if st.button("추첨 하러 가기"):
        go_to_page(3)

# Page 3: 박스 고르기 - 모바일 최적화 + 이미지 깨짐 해결 버전
if st.session_state.page == 3:
    st.subheader("아버님! 원하는 럭키박스를 선택해주세요!")
    
    cols = st.columns(4)  # 한 줄에 4개씩 배치
    for i in range(8):  # 총 8개의 박스
        with cols[i % 4]:
            # 박스 이미지 표시 (Streamlit 기본 image 함수 사용)
            st.image("./page3.png", width=60)  # width=60px 로 모바일 최적화
            
            # 박스 아래 '선택' 버튼
            if st.button("선택", key=f"box_{i}"):
                st.session_state.result = prizes[0]  # 무조건 신차 인수권 당첨
                go_to_page(4)  # 결과 페이지로 이동

# Page 4
if st.session_state.page == 4:
    st.subheader("🎊 결과 발표 🎊")
    st.success(f"""당첨된 선물은 바로...

## {st.session_state.result}""")
    if "신차 인수권" in st.session_state.result:
        st.markdown("### 🎉 아버님 어머님! 축하드립니다! 🎉")
        st.markdown("### 지금 바로 출발하시죠! 🚗")

    if st.button("처음으로 돌아가기"):
        st.session_state.page = 1
        if "shuffled_prizes" in st.session_state:
            del st.session_state.shuffled_prizes
        st.rerun()
