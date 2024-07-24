import streamlit as st

st.title('my first streamlit app')
name = st.text_input('이름을 입력하세요:')

menu = st.selectbox('좋아하는 음식을 선택하세요:', ['망고 빙수', '꿔바로우', '상하이치킨버거', '아몬드 봉봉'])

if st.button('인사말 생성') :
    st.write(f'안녕하세요, {name}님! 당신의 좋아하는 음식은 {menu}입니다. 오늘도 좋은 하루 보내세요!')
