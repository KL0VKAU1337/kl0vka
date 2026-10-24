import streamlit as st

st.set_page_config(page_title="мое супер веб приложение", page_icon="🤩", layout="wide")

st.title("добро пожаловать в наше веб приложение ")

tab1, tab2 = st.tabs(["про меня", "мой инструмент"])

with tab1:
    st.header("знакомство с автором")
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("https://img3.stockfresh.com/files/c/cookelma/m/67/1316173_stock-photo-ridiculous-dog-dj.jpg", width=200)
    with col2: 
        st.subheader("привет я будущий python developer")
        st.write("я учусь в малой компютерной академии II STEP")