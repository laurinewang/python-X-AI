import streamlit as st
import os

folderpath = "markdown"  # 設定資料夾路徑
files = os.listdir(folderpath)  # 取得資料夾內所有檔案
print(files)

files.sort()  # 將清單排序,預設由小到大


for f in files:  # ['class1-1.md','class1-2.md']逐一讀取所有 .md案檔
    # markdown/class2.md
    with open(f"{folderpath}/{f}", "r", encoding="utf-8") as files:
        content = files.read()

    with st.expander(f[:-3]):  # 使用expander,標題為案檔名稱去掉.md
        st.write(content)  # 將檔案顯示在網頁上
