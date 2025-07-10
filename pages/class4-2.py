import streamlit as st

st.title("🍔 點餐機")

if "menu" not in st.session_state:
    st.session_state.menu = []

# 左輸入框，右加入按鈕
col1, col2 = st.columns([4, 1])
with col1:
    food = st.text_input("輸入餐點名稱")
with col2:
    if st.button("加入") and food:
        st.session_state.menu.append(food)
        st.rerun()

# 顯示購物籃
if st.session_state.menu:
    for i in range(len(st.session_state.menu)):
        col1, col2 = st.columns([5, 1])
        with col1:
            st.write("🍴 " + st.session_state.menu[i])
        with col2:
            if st.button("刪除", key=f"del{i}"):
                st.session_state.menu.pop(i)
                st.rerun()
else:
    st.write("購物籃是空的")
