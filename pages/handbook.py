import streamlit as st

with st.expander("class1 的筆記"):
    st.write(
        '''
### Python 基本筆記
#### 1. 註解

- **註解**是用來幫助你記錄程式內容的文字，程式不會執行它們。

  - **單行註解**：使用 `#` 來寫一行註解。
  - **多行註解**：可以用 `"""` 或 `\'\'\'` 包起來，寫很多行的註解。

```python
# 這是單行註解
print("Hello World")  # 這行程式會顯示文字
"""
這是多行註解
你可以寫很多行文字
"""
```

#### 2. 顯示文字

- `print()` 是一個可以讓我們顯示文字或數字的指令。

```python
print("Hello World")  # 顯示文字
```

#### 3. 數字與資料類型

- **整數 (int)**：像是 1、2、3 這樣的數字。

  ```python
  print(1)  # 顯示 1
  ```

- **浮點數 (float)**：像是 1.0、1.23 這樣的小數。

  ```python
  print(1.0)  # 顯示 1.0
  print(1.123)  # 顯示 1.123
  ```

- **字串 (str)**：一串文字或單字，放在雙引號 `" "` 裡面。

  ```python
  print("apple")  # 顯示 apple
  ```

- **布林值 (bool)**：只有 `True` 或 `False`，用來表示真假。

  ```python
  print(True)  # 顯示 True
  print(False)  # 顯示 False
  ```

#### 4. 變數

- **變數**就像是一個用來存東西的盒子，裡面可以放數字、文字或其他資料。
- 用 `=` 來把資料放進變數裡。

```python
a = 10  # 將數字 10 存入變數 a
print(a)  # 顯示 a 裡的數字 10
a = "apple"  # 現在變數 a 裡是 "apple"
print(a)  # 顯示 a 裡的 "apple"
```

#### 5. 運算子

- **加法 (+)**：將數字加在一起。

  ```python
  print(1 + 1)  # 顯示 2
  ```

- **減法 (-)**：將數字相減。

  ```python
  print(1 - 1)  # 顯示 0
  ```

- **乘法 (\*)**：將數字相乘。

  ```python
  print(1 * 1)  # 顯示 1
  ```

- **除法 (/)**：將數字相除。

  ```python
  print(1 / 1)  # 顯示 1.0
  ```

- **次方 (**)\*\*：將數字提升到某個次方。

  ```python
  print(2 ** 3)  # 顯示 8 (2 的 3 次方)
  ```

- **取餘數 (%)**：除法後剩下的數字。

  ```python
  print(5 % 2)  # 顯示 1 (5 除以 2 餘數是 1)
  ```

- **取整 (//)**：除法後，只保留整數部分。

  ```python
  print(5 // 2)  # 顯示 2
  ```

#### 6. 優先順序

在算式中，有些運算會先做，這叫做**優先順序**：

1. **括號 ()**：最先計算。
2. **次方 (**)\*\*
3. **乘、除、取餘數、取整** (`*`, `/`, `%`, `//`)
4. **加、減** (`+`, `-`)

例如：

```python
print(2 + 3 * 4)  # 會先做 3*4，再加 2，結果是 14
```

#### 7. 字串拼接

- **字串拼接**是把兩個字串合在一起，變成一個新的字串。

```python
a = "good"
b = "night"
print(a + b)  # 顯示 "goodnight"
```

#### 8. 字串格式化

- **字串格式化**讓我們可以把變數放進字串中，像這樣：

```python
name = "laurine"
age = 13
print(f"hello, my name is {name}, I am {age} years old.")  # 顯示 "hello, my name is laurine, I am 13 years old."
name="rosie"
age="11"
print(f"hello, my name is {name}, I am {age} years old.")
```
'''
    )


with st.expander("class2 的筆記"):
    st.write(
        """
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

"""
    )
