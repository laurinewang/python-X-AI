"""
這是多行註解
可以放很多文字
"""

# 這是單行註解
print("Hello World")  # print是在終端機顯示文字的指令
# ctrl+?可以快速/取消註解

print(1)  # int這是整數 -1 0 1 2 3 4 5 6 7 8 9
print(1.0)  # float這是浮點數
print(1.123)  # float這是浮點數
print("apple")  # str這是字串
print(True)  # bool這是布林值True/False
print(False)  # bool這是布林值True/False

# 變數
a = 10  # 新增一個儲存空間並取名為a,"="的功能是將右邊的值10存入左邊的a
print(a)  # 在終端機顯示a所存的值
a = "apple"  # 將右邊apple存入左邊的a

# 運算子
print(1 + 1)  # 加法
print(1 - 1)  # 減法
print(1 * 1)  # 乘法
print(1 / 1)  # 除法
print(1**1)  # 次方
print(1 % 1)  # 取餘數
print(1 // 1)  # 取整
# 優先順序
# 1()括號
# 2**次方
# 3*/%//乘 除  取整 取餘數
# 4+- 加減

a = "good"
b = "night"
print(a + b)
a = "py"
b = "thon"
print(a + b)

# 字串格式化
name = "laurine"
age = 13
print(f"hello, my name is {name} ,I am {age} years old.")  # f-string
