# 比較運算子,只能同樣類型作比較
print(1 == 1)  # True
print(1 != 1)  # False
print(1 > 1)  # False
print(1 < 1)  # False
print(1 >= 1)  # True
print(1 <= 1)  # True

##邏輯運算子
print(True and True)  # True
print(True and False)  # False
print(False and True)  # False
print(False and False)  # False

# or運算子
print(True or True)  # True
print(True or False)  # True
print(False or True)  # True
print(False or False)  # False

# not運算子
print(not True)  # False
print(not False)  # True

# 優先順序
# 1()括號
# 2**次方
# 3*/%//乘 除  取整 取餘數
# 4+- 加減
# 5==!=> < >= <=比較運算子
# 6 not
# 7 and
# 8 or

# 密碼門檢查
password = input("請輸入密碼:")
if password == "goyounjung":
    print("hell0")
elif password == "goyounjung2":  # 前面的條件都沒達成時,會執行這個條件判斷
    print("hell1")
elif password == "goyounjung3":  # 前面的條件都沒達成時,會執行這個條件判斷
    print("hell2")
else:  # 如果密碼不正確，則執行下面的指令
    print("0422")
