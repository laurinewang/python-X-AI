import streamlit as st

# st.number_input()讓使用者可以輸入數字,可以進行以下設定
# step=1,可以讓使用者只能輸入整數
# min_value=1,可以讓使用者輸入的數字最小值為0
# max_value=100,可以讓使用者輸入的數字最大值為100
number = st.number_input("請輸入一個數字:", step=1, min_value=1, max_value=100)
# 顯示讓使用者輸入數字,
st.write(f"你輸入的數字是{number}")
st.write("---")

st.write("## 練習")
s = st.number_input("請輸入分數:", step=1, min_value=1, max_value=100)
if s >= 90:
    st.write("你的等級是A")
elif s >= 80:
    st.write("你的等級是B")
elif s >= 70:
    st.write("你的等級是C")
elif s >= 60:
    st.write("你的等級是D")
else:
    st.write("你的等級是E")
