🧠 判斷語法 if / elif / else
🔸 if 是「如果...就...」的意思
我們可以根據不同的情況，做不同的事情。

if 條件:
做某件事
🔸 多個 if：每一個都會檢查
if 條件 1:
做事情 1
if 條件 2:
做事情 2
✅ 每一個都會檢查。

🔸 elif 是「不然如果...就...」
if 條件 1:
做事情 1
elif 條件 2:
做事情 2
else:
其他的情況
✅ 用 elif 可以省時間，只要前面的條件成立，就不會再檢查後面。

🔁 for 迴圈：重複做事情
🔸 基本用法：
for i in range(5):
print(i)
print("hello")
👆 上面會印出：

0
hello
1
hello
...
4
hello
🔸 range 的三種寫法：
range(5) → 從 0 到 4（總共 5 次）

range(1, 5) → 從 1 到 4

range(1, 10, 2) → 從 1 開始，每次 +2，到 9 為止（會印出 1, 3, 5, 7, 9）

🌐 Streamlit：做網頁小工具
🔸 按鈕
import streamlit as st

if st.button("點我"):
st.balloons()
✅ 點按鈕後，畫面上會出現氣球！

🔸 數字金字塔
num = st.number_input("請輸入一個數字", 1, 9)

for i in range(1, num + 1):
st.write(f"{i}" \* i)
👆 如果輸入 3，會印出：

1  
22  
333
📦 List（清單）
🔸 List 是放很多東西的箱子
a = [1, 2, 3]
b = [1, "apple", True]
🔸 位置（index）從 0 開始
L = [1, 2, 3, "a", "b", "c"]
print(L[0]) # 印出 1
print(L[3]) # 印出 "a"
🔸 切片：選出一部分
L[::2] # 每隔一個選一次 → [1, 3, 'b']
L[1:4] # 從第 1 個到第 3 個 → [2, 3, 'a']
L[1:4:2] # 每隔一個選一次 → [2, 'a']
🔸 list 的長度 & 修改元素
len(L) # 算裡面有幾個東西
L[0] = 99 # 把第 0 個改成 99
🔸 用 for 讀出 list 的每個東西
for i in range(len(L)):
print(L[i])
或是：

for item in L:
print(item)
🔸 加入新元素：append()
L.append("新東西")
🔸 移除元素：
remove("想刪的東西")：刪掉第一個出現的東西

pop()：刪掉最後一個

🔸 排序：sort()
L = [3, 1, 4, 2]
L.sort()
print(L) # [1, 2, 3, 4]
🧠 變數是怎麼記住東西的？
🔸 Call by value（數字、字串）
a = 1
b = a
b = 2
print(a, b) # a 還是 1，b 是 2
🔸 Call by reference（list）
a = [1, 2, 3]
b = a
b[0] = 9
print(a) # a 也跟著變
✅ 解法：用 copy()

b = a.copy()
📂 檔案操作 open()
開啟檔案的方式：
模式 說明
r 讀取
w 寫入（會清空原本的）
a 追加內容
f = open("檔案路徑", "r", encoding="utf-8")
內容 = f.read()
print(內容)
f.close()
✅ 更簡單的寫法：

with open("檔案路徑", "r", encoding="utf-8") as f:
內容 = f.read()
print(內容)
🧰 字串小工具
endswith()：檢查結尾是不是某個字
filename = "note.md"
print(filename.endswith(".md")) # True
'''
