# 算術指定運算子
a = 1
a += 1  # a=a+1
print(a)  # 2
a -= 1  # a=a-1
print(a)  # 1
a *= 2  # a=a*2
print(a)  # 2
a /= 2  # a=a/2
print(a)  # 1.0
a //= 2  # a=a//2
print(a)  # 0
a %= 2  # a=a%2
print(a)  # 0.0
a **= 2  # a=a**2
print(a)  # 0.0

# 優先順序
# 1()括號
# 2**次方
# 3*/%//乘 除  取整 取餘數
# 4+- 加減
# 5==!=> < >= <=比較運算子
# 6 not
# 7 and
# 8 or
# 9 = +=-=*=/=%//=%=**=算術指定運算子

# while循環
# while會搭配一個條件式來使用
# 條件式為True 時會一直執行迴圈
# 條件式為False 時會跳出迴圈
# 每次執行迴圈玩都會重新檢查條件有沒有變成False
i = 0
while i < 5:
    print(i)
    i += 1  # i=i+1

# break強制跳出迴圈
# 先判斷break屬於哪個迴圈,然後跳出該迴圈
i = 0
while i < 5:
    print(i)
    for j in range(5):
        print(j)
    if j == 3:
        break  # 跳出迴圈,屬於while迴圈
    i += 1  # i=i+1

for i in range(5):
    print(i)
    if i == 3:
        break  # 跳出迴圈

    import random  # 引入random模組

# random.randrange設定抽籤範圍的方式跟range()一樣
print(random.randrange(7))  # 0~6
print(random.randrange(1, 7))  # 1~6
print(random.randrange(1, 7, 2))  # 1~6,尖閣2

# print(random.randint()設定抽籤範圍的方式一定要設定開始與結束
# 且結束的數字會包含在內
print(random.randint(1, 6))  # 1~6

ans = random.randint(1, 100)  # 產生一個1~100的隨機數
while True:  # 無窮迴圈
    num = int(input("請輸入1~100的數字:"))
    if num < 0 or num > 100:
        print("請輸入1~100的數字")
    elif num > ans:  # 如果輸入的數字大於答案
        print("太大了")
    elif num < ans:  # 如果輸入的數字小於答案
        print("太小了")
    else:  # 如果輸入的數字等於答案
        print("恭喜你,答對了")
        break  # 跳出無窮迴圈

    #(dictionary)字典:字典是一個對應式的集合,用來儲存[key-value]
    #字典很適合用來表示有對應關西的資料,向式商品和價格

    # 字典的建立方式:使用大擴號{} ,key 和 value 之間用冒號 : 分隔
    d = {"apple": 1, "banana": 2, "cherry": 3}
    print(d)  # {'apple': 1, 'banana': 2, 'cherry': 3}

    # 字典的取得特定key 的value
    #如果 key 不存在會產生 keyError 錯誤
    d = {"apple": 1, "banana": 2, "cherry": 3}
    print(d["apple"])  
    #print(d["orange"])  #這行會產生 keyError:"orange"

    
    #print(d["banana"])  # 2
    #遍曆dictionary:有多種方式可以走訪dictionary中的資料
    d={"apple":1,"banana":2,"cherry":3}
    
    #way1 直接遍曆dictionary,會取得所有key
    for key in d:
        print(key)#印出key名稱
        print(d[key])#用key來取得所有對應的value
    #way2 明確使用 key(),會取得所有value
    for k in d.keys():
        print(k)#印出key名稱
        print(d[k])#用key來取得所有對應的value

    #way3使用values() 方法來取得的所有value 
    for v in d.values():
        print(v)#印出value, 但不知道對應的key是甚麼

    #way4 use items()方法取得所有key-value
    #這是最常用的方式,because 可以同時存取 key-value
    for k,v in d.items():
        print(k,v) #同時印出key和value

    #新增/修改dictionary 內容
    # 直接指定 key 對應的value, if key 不存在會創建一個新的key
    d={"apple":1,"banana":2,"cherry":3}
    d["apple"]=10 #修改[apple]對應的value
    print (d)
    d=["蓮霧"] = 15 # 新增一個key-value 配對
    print(d)

    #刪除字典內容
    d={"apple":1,"banana":2,"cherry":3}
    d.pop("apple") #刪除[apple]
    #如果要刪掉的key不存在,會出現keyError,
    #這時候可以加上第二個參數,當key不存在時,不會有任何變化
    popitem=d.pop("蓮霧","不存在這筆資料") # 不會有任何變化
    print(d) #{"banana":2,"cherry":3}
    print(popitem) # 不存在這筆資料
    


    

