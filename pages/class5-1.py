# len:取得dictiionary中有多少組key-value 配對
d = {"apple": 1, "banana": 2, "cherry": 3}
print(len(d))  # 3 dictiionary中有3組key-value 配對

# 檢查抹個key是否存在於dictionary
# 使用前先檢查可以避免keyError錯誤
d = {"apple": 1, "banana": 2, "cherry": 3}
print("apple" in d)  # True apple key存在
print("orange" in d)  # False orange key不存在

# 檢查抹個元素中是否存在於list 中
# 使用in 可以快速檢查抹個元素否存在於list 中
l = [1, 2, 3, 4, 5]
print(2 in l)  # True,3在list 中

# 比較複雜的dict
d = {
    "a": [1, 2, 3],
    "b": {"c": 4, "d": 5},
}
print(d["a"])  # [1,2,3]
print(d["a"][0])  # 1
print(d["b"])  # {"c":4,"d":5}
print(d["b"]["c"])  # 4

# 成績登記系統,key是Studentname, value是student的成績,每個科目有3個成績
grade = {
    "apple": {"math": [90, 80, 70], "english": [80, 70, 60], "physics": [70, 60, 50]},
    "banana": {"math": [80, 70, 60], "english": [70, 60, 50], "physics": [60, 50, 40]},
    "cherry": {"math": [70, 60, 50], "english": [60, 50, 40], "physics": [50, 40, 30]},
}

# 取得apple的math成績
print(grade["apple"]["math"])  # [90,80,70]
# 取得banana的physics成績
print(grade["banana"]["physics"])  # [60,50,40]
# 取得cherry的english成績
print(grade["cherry"]["english"])  # [60,50,40]
