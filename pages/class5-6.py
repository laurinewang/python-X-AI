import streamlit as st
import openai
from dotenv import load_dotenv
import os

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

if "history" not in st.session_state:
    st.session_state.history = []

if "system_message" not in st.session_state:  # 初始化系統訊息
    # 如果系統訊息不存在,則使用預設的系統訊息
    st.session_state.system_message = "請用繁體中文進行後續對話"

# 設置三個烈布局,分別占用6:1的寬度

col1, col2 = st.columns([6, 1])

with col1:
    # 在第一列顯示病根新系統訊息
    st.session_state.system_message = st.text_input(
        "系統訊息", st.session_state.system_message
    )

with col2:
    if st.button("清除紀錄"):  # 在第三列顯示清除按鈕
        st.session_state.history = []  # 按下按鈕後清空對話紀錄
        st.rerun()  # 重新整理畫面一反應跟改

# 從對話紀錄中帶每個訊息並顯示
for message in st.session_state.history:
    if message["role"] == "user":  # 如果訊息的腳色是使用者
        st.chat_message("user", avatar="👤").write(message["content"])
    # 顯示使用者訊息
    else:
        st.chat_message("assistant", avatar="🤖").write(message["content"])
        # 顯示AI訊息,使用指定頭像

prompt = st.chat_input("請輸入你的訊息")  # 顯示對話輸入框,等待使用者輸入訊息
if prompt:  # 如果使用者輸入了訊息
    st.session_state.history.append({"role": "user", "content": prompt})
    # 將訊息加入到對話紀錄

    response = openai.chat.completions.create(
        model="gpt-4o-mini-search-preview",  # 使用選定AI模型
        messages=[{"role": "system", "content": st.session_state.system_message}]
        + st.session_state.history,
    )

    assistant_message = response.choices[0].message.content  # 取得AI回傳的訊息內容
    st.session_state.history.append({"role": "assistant", "content": assistant_message})
    # 將AI回傳的訊息加入到對話紀錄
    st.rerun()  # 重新整理畫面顯示新訊息
