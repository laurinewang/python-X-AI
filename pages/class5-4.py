import streamlit as st

st.chat_message("user").write("這是顯示給使用者的訊息")
st.chat_message("assistant").write("這是AI的訊息")

# 範例對話紀錄
history = [
    {"role": "user", "content": "你好,AI!"},
    {"role": "assistant", "content": "你好,使用者!"},
    {"role": "user", "content": "我是使用者,你是AI!"},
    {
        "role": "assistant",
        "content": "st.chat_message().write('我是AI,你是使用者!')",
    },
]

# 用迴圈顯示聊天泡泡
for message in history:
    if message["role"] == "user":
        st.chat_message("user", avatar="👤").write(message["content"])
    else:
        st.chat_message("assistant", avatar="🤖").write(message["content"])
