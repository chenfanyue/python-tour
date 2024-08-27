## 集合的创建
# 从字面量创建集合
fruits = {"apple", "banana", "cherry"}
print(fruits)  # 输出：{'banana', 'cherry', 'apple'}

# 从可迭代对象创建集合
iterable = ["apple", "banana", "cherry", "apple"]
fruits_set = set(iterable)
print(fruits_set)  # 输出：{'banana', 'cherry', 'apple'}

# 创建空集合
empty_set = set()
print(type(empty_set))  # 输出：<class 'set'>


## 集合的基本操作
# add
fruits = {"apple", "banana"}
fruits.add("cherry")
fruits.add('apple')
print(fruits)  # 输出：{'banana', 'cherry', 'apple'}

# update 批量添加
fruits = {"apple", "banana"}
iterable = {"cherry", "orange"}
fruits.update(iterable)
print(fruits)  # 输出：{'banana', 'cherry', 'apple', 'orange'}

# in
fruits = {"apple", "banana", "cherry"}
print('apple' in fruits) # True

# remove, discard
fruits = {"apple", "banana", "cherry"}
fruits.remove('banana')
fruits.discard("banan")
print(fruits)  # 输出：{'cherry', 'apple'}

# pop 随机删除
fruits = {"apple", "banana", "cherry"}
removed_item = fruits.pop()
print(removed_item)  # 输出：集合中的某个元素（随机）
print(fruits)  # 输出剩余的集合

# clear
fruits = {"apple", "banana", "cherry"}
fruits.clear()
print(fruits)  # 输出：set()

# `del` instruction
fruits = {"apple", "banana", "cherry"}
del fruits
# print(fruits)  # 会引发 NameError，因为集合已被删除


## 集合的运算
# union |
set1 = {"apple", "banana"}
set2 = {"cherry", "banana"}
union_set = set1.union(set2)
# 或者 union_set = set1 | set2
print(union_set)  # 输出：{'cherry', 'banana', 'apple'}

# intersection &
set1 = {"apple", "banana"}
set2 = {"cherry", "banana"}
intersection_set = set1.intersection(set2)
# 或者 intersection_set = set1 & set2
print(intersection_set)  # 输出：{'banana'}

# difference -
set1 = {"apple", "banana"}
set2 = {"cherry", "banana"}
difference_set = set1.difference(set2)
# 或者 difference_set = set1 - set2
print(difference_set)  # 输出：{'apple'}

# symmetric_difference ^
set1 = {"apple", "banana"}
set2 = {"cherry", "banana"}
sym_diff_set = set1.symmetric_difference(set2)
# 或者 sym_diff_set = set1 ^ set2
print(sym_diff_set)  # 输出：{'cherry', 'apple'}
