# 連續使用if跟使用if elif else 的差別
# elif 可以排除前面有判斷過的條件,縮短判斷條件的複雜度,時間也減少
# 但是如果是使用多個if來執行,則每個if都會被執行,效率較低

# for 迴圈
# for 搭配in, in 後面接一個有範圍的東西
# rrange(5) 從0開始,每次加1,到5為止
# i 是迴圈的變數可以自己取名
# 回圈變數每回合從範圍裡取一個資料出來
for i in range(5):
    print(i)
    print("hello")

# range 可以設定起始值與結束值,但不會包含結束值
# range(1,5)產生1234
for i in range(1, 5):
    print(i)
    print("hello")
# range 可以設定起始值與結束,但不會包含結束值
# range(1,10,2)產生13579
for i in range(1, 10, 2):
    print(i)
