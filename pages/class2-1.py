print(len("apple"))  # len是一個函式,可計算字串的長度
print(len("ㄎ"))  # len()是一個函式,可計算字串的長度
# type()可以查看變數的型態
print(type(1))  # <class 'int'>
print(type(1.0))  # <class 'float'>
print(type("apple"))  # <class 'str'>
print(type(True))  # <class 'bool'>

# 型態轉換
print(int(1.0))  # float轉int
print(float(1))  # int轉float
print(str(1))  # int轉str
print(str("1.234"))  # float轉str
print(bool(1.0))  # float轉bool True
print(bool(1))  # int轉bool
print(bool(0))  # float轉bool


# () 是函式的使用
print("輸入開始")
# input()是一個函式,可以讓使用者輸入文字
# ()
a = input("請輸入你的名字:")
print("輸入結束")
print(int(a) + 10)
print(type(a))  # 透過input()可以輸入文字
