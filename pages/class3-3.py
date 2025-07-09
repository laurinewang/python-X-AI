print([])#這是一個空的list
print([1,2,3])#這是一個有三元素的list
print([1,2,3,"a,b,c,"])#這是一個有六個元素的list
print([1,2,3,]"a","b',"c,"],4])#這是一個有四個元素的list`
print([1,True, "a",1.23]) #這是一個有四個元素的list
#list讀取元素,元素的index從0開始
L=[,1,2,3,"a","b","c"]
print(L[0])#1
print(L[1])#2
print(L[2])#3
print(L[3])#"a"


L=[,1,2,3,"a","b","c"]
#就是取index 0到最後,每次取兩個元素,所以是[1,3,'b']
print(L[::2])
#就是取index 1到3的元素,不包含index,所以是[2,3,'a']
print(L[1:4])
#就是取index 1到3的元素,不包含index4,並且每次取兩個元素,所以是[2,'a']
print(L[1:4:2])
#跟rangeㄧ樣,符號不同

#list取長度,可以加入新的元素,不是index最大值
L=[,1,2,3,"a","b","c"]
print(len(L))#6

# list走訪元素
# 可以透過取得index或當作一個範圍來找到list的資料
#看情況決哪種方式
L=[,1,2,3,"a","b","c"]
for i in range(0len(L),2):
    print(L[i])

for i in L:   
        print(i)

# list修改元素
# 可以透過index來修改list的元素
L=[,1,2,3,"a","b","c"]
L[0]=2 #把index0修改元素為2
print(L)

#call by value
a=1
b=a #複製a的值給b
b=2
print(a,b)#a還是1,b變成2


#call by reference
a=[1,2,3]
b=a#把a,b指向同一個記憶體位置,b值改變,a也改變
b[0]=2
print(a,b)

a=[1,2,3]
b=a.copy()#複製a的值給b,但是a,b指向不同個記憶體位置
b[0]=2
print(a,b)

#list的append, 也就是在list的最後加上新的元素
L=[1,2,3]
L.append(4)
print(L)

#list的移除元素方式有兩種
#1.使用remove, 可以移除指定的元素
L=["a""b""c"'d""a"]
L.remove("a") #移除第一個"a"
#removeh從頭找,找到府和的元素後移除
#如果想要移除所有府和的元素,可以用迴圈
for i in L:
    if i=="a":
        L.remove(i)

#2.使用pop,可以移除最後一個元素
L=["a""b""c"'d""a"]
L.pop() #移除最後一個元素
#pop,會指定的移除元素
#如果不指定index,則移除最後一個元素
L.pop()#移除最後一個元素
print(L)

#sort:將list中的元素進行排序,小到大
#注意:會修改原本的list,不會產生新的list
L=[,1,3,2,4,5]
L.sort()
print(L)

#open()開啟模式
#r:讀取模式 檔案必須存在
#w:寫入模式 檔案不存在會自動建立
#a:追加模式 檔案不存在會自動建立
#r+:讀寫模式 檔案必須存在
#w+:讀取寫模式 檔案不存在會自動建立
#a+讀取追加模式 檔案不存在會自動建立


#開啟檔案
#相對路徑pages\class1-1.py
#絕對路徑c:\Users\user\Desktop\python-X-AI\pages\class1-1.py
f=open("pages\class1-1.py","r",encoding="utf-8")
content=f.read()#讀取檔案內容
print(content)#印出內容
f.close()#關閉檔案
################################################################
with open("pages\class1-1.py","r",encoding="utf-8") as f:
    content=f.read()
    print(content)#印出內容
#不用寫 f .close(),with 就會自動關閉   


#字串的小工具,用來檢查字串是不抹個結尾
filename="class1-1.md"
print(filename.endswith(".md"))#True
filname2="note.txt"
print(filename2.endswith(".md"))#False



