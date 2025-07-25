import streamlit as st

st.write("### 按鈕練習")
# st.write()可以在網頁上顯示一個按鈕,使用者可以點擊案紐
# key可以辨識按鈕的名稱,可以用來驅分不同按鈕
# 如果使用者點及按鈕,st.botton()會回傳True,否則回傳False
st.button("點我", key="button1")
if st.button("點我", key="button2"):
    st.balloons()
if st.button("點我", key="button3"):
    st.snow()

st.write("---")

st.write("### 數字金字塔")

num = st.number_input("請輸入一個數字:(1到9)", min_value=1, max_value=9, step=1)
for i in range(1, num + 1):
    st.write(f"{i}" * i)
