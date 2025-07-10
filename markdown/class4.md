# 🐍【今天的 Python 小筆記】👦👧

---

## ✏️ 一、算術指定運算子（簡單說：讓變數自己加減乘除）

```python
a = 1
a += 1  # a = a + 1，a 自己加 1
a -= 1  # a = a - 1，a 自己減 1
a *= 2  # a = a * 2，a 自己乘以 2
a /= 2  # a = a / 2，a 自己除以 2
a //= 2  # 整數除法，不留小數點
a %= 2   # 求餘數（除完之後剩下多少）
a **= 2  # 做次方，像 2 的 3 次方就是 2*2*2
```

👉 **小提醒：** 用這些可以讓一個變數自己改變數字，很像計分板自動加減分！

---

## 🧮 二、運算的順序

像算數題一樣，電腦也有「先算誰、後算誰」的規則：

1. `()` 括號裡的先算
2. `**` 次方
3. `* / % //` 乘、除、餘數、整除
4. `+ -` 加減
5. 比大小：`== != > < >= <=`
6. `not` 不是
7. `and` 和
8. `or` 或
9. `= += -= ...` 最後才是「指定值」這些

---

## 🔁 三、重複做的事：while 迴圈

```python
i = 0
while i < 5:
    print(i)
    i += 1  # i 自己加 1
```

🔹 `while` 會一直重複做事情，**只要條件是對的（True）**
🔸 上面這段會印出 0 到 4，因為當 i 變成 5 就不會再繼續了！

---

## ⛔ 四、跳出迴圈：break

```python
for i in range(5):
    if i == 3:
        break  # 當數字是 3，就停止
```

🔹 `break` 的意思就是「不玩了，馬上離開這圈圈」。

---

## 🎲 五、random 模組：隨機數字（像抽籤）

```python
import random

print(random.randrange(1, 7))  # 像骰子 1~6（不含 7）
print(random.randint(1, 6))    # 一樣是 1~6，但含 6
```

🔸 `randrange()` 是不包含最後一個數
🔸 `randint()` 是包含最後一個數

---

## 🎯 六、猜數字遊戲（綜合練習）

```python
ans = random.randint(1, 100)

while True:
    num = int(input("請輸入1~100的數字:"))
    if num < 0 or num > 100:
        print("範圍錯了！")
    elif num > ans:
        print("太大了")
    elif num < ans:
        print("太小了")
    else:
        print("答對了！")
        break
```

👉 這是一個可以玩的遊戲，電腦想一個數字，讓你一直猜，猜對才會跳出。

---

## 📚 七、字典 Dictionary（像寶可夢圖鑑：名稱＋資料）

```python
d = {"apple": 1, "banana": 2, "cherry": 3}
```

🔹 `字典` 是一種資料，長得像：名字 → 數字
🔸 像「apple 是 1 元」、「banana 是 2 元」

---

### ✅ 怎麼用字典

#### 1. 拿出資料

```python
print(d["apple"])  # 印出 1
```

#### 2. 走訪整個字典

```python
for key in d:
    print(key)        # 印出名字
    print(d[key])     # 印出價格
```

#### 3. 同時看名字和價格

```python
for k, v in d.items():
    print(k, v)  # 印出 apple 1、banana 2 ...
```

---

### 🆕 加入或改資料

```python
d["apple"] = 10  # 把 apple 改成 10 元
d["watermelon"] = 15  # 新增一個水果
```

---

### ❌ 刪除資料

```python
d.pop("apple")  # 刪掉 apple
```

🔸 如果 key 不在，可以加第二個參數：

```python
d.pop("peach", "沒這項資料")  # 不會報錯
```

---

# 🎉 總結：今天學會了什麼？

| 題目         | 學到什麼                                    |
| ------------ | ------------------------------------------- |
| `+= -= *=`   | 自己加減乘除的簡寫                          |
| `while`      | 重複做某件事，直到不成立                    |
| `break`      | 馬上跳出迴圈，不玩了                        |
| `random`     | 抽隨機數，做遊戲超好用                      |
| `dictionary` | 用 key-value 記錄一對一資料（像名稱跟價格） |

---
