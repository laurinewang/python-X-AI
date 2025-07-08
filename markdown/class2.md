# 🐍 Python 課堂筆記

## ✨ 1. 基本函式介紹

### 🧮 `len()` – 看字有多長

```python
print(len("apple"))  # 5
print(len("ㄎ"))     # 1
```

✅ `len()` 是用來算「字串」有幾個字。

---

### 🔍 `type()` – 看東西是什麼類型

```python
print(type(1))        # 整數 int
print(type(1.0))      # 小數 float
print(type("apple"))  # 字串 str
print(type(True))     # 布林值 bool（只有 True 或 False）
```

---

### 🔁 型態轉換 – 變來變去

```python
print(int(1.0))     # 變成整數
print(float(1))     # 變成小數
print(str(1))       # 變成文字
print(bool(1))      # True
print(bool(0))      # False
```

---

## 🎤 2. 輸入與輸出

### ✏️ `input()` – 讓使用者輸入東西

```python
a = input("請輸入你的名字:")
print("你輸入的是", a)
```

🔺 注意：輸入的東西都是「文字型別 str」，要換成數字才能加減乘除。

---

## 💬 3. Streamlit 介紹（做互動式網頁）

```python
import streamlit as st
```

### 📝 顯示文字的幾種方式：

- `st.write()` ➤ 顯示文字、數字、表格等（萬用）
- `st.text()` ➤ 顯示純文字（不能加粗、不能加連結）
- `st.markdown()` ➤ 可以加粗、斜體、連結、程式碼
- `st.title()` ➤ 顯示大標題

### 💡 顯示提示訊息

- `st.info()` ➤ 藍色小提醒
- `st.success()` ➤ 綠色成功訊息
- `st.warning()` ➤ 橘色警告訊息
- `st.error()` ➤ 紅色錯誤訊息

---

## ➕ 4. 比較與邏輯運算

### 比較運算子（比大小用的）

```python
==  相等
!=  不相等
>   大於
<   小於
>=  大於等於
<=  小於等於
```

### 邏輯運算子（多個條件一起判斷）

```python
and  並且（全部都要對才算對）
or   或者（有一個對就算對）
not  反過來（True 變 False）
```

---

## ⚙️ 5. 執行順序（運算優先順序）

1. 括號 `()`
2. 次方 `**`
3. 乘、除、整除、餘數 `* / // %`
4. 加減 `+ -`
5. 比較 `== != > < >= <=`
6. `not`
7. `and`
8. `or`

---

## 🔐 6. 密碼門檻（if 判斷式）

```python
password = input("請輸入密碼:")
if password == "goyounjung":
    print("hell0")
elif password == "goyounjung2":
    print("hell1")
elif password == "goyounjung3":
    print("hell2")
else:
    print("密碼錯誤")
```

✅ 用 `if`, `elif`, `else` 讓程式做不同決定。

---

## 🔢 7. Streamlit 數字輸入與等級判斷練習

```python
number = st.number_input("請輸入一個數字:", step=1, min_value=1, max_value=100)
st.write(f"你輸入的數字是 {number}")
```

### 🎯 分數轉等級

```python
s = st.number_input("請輸入分數:", step=1, min_value=1, max_value=100)
if s >= 90:
    st.write("你的等級是 A")
elif s >= 80:
    st.write("你的等級是 B")
elif s >= 70:
    st.write("你的等級是 C")
elif s >= 60:
    st.write("你的等級是 D")
else:
    st.write("你的等級是 E")
```
