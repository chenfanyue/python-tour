## 列表的创建
my_list = [1, 2, 3, 4]

# list(iterable)
my_list = list([1, 2, 3, 4])
my_list = list(range(1, 5))  # 生成 [1, 2, 3, 4]

empty_list = []
empty_list = list()


## 列表的基本操作
my_list = [1, 2, 3, 4]
print(my_list[0])  # 输出 1
my_list[-1]

my_list[0] = 10
print(my_list)  # 输出 [10, 2, 3, 4]

my_list.append(5)
print(my_list)  # 输出 [10, 2, 3, 4, 5]

my_list.insert(1, 20)
print(my_list)  # 输出 [10, 20, 2, 3, 4, 5]

my_list.remove(20)
print(my_list)  # 输出 [10, 2, 3, 4, 5]

my_list.pop(0)
print(my_list)  # 输出 [2, 3, 4, 5]

my_list = [1, 2, 3, 4]
popped_item = my_list.pop()
print(popped_item) # 4
print(my_list) # [1, 2, 3]

my_list.clear()
print(my_list)  # 输出 []


## 列表的切片操作
my_list = [1, 2, 3, 4, 5]
sub_list = my_list[1:4]  # 获取索引 1 到 3 的元素，输出 [2, 3, 4]

my_list = [1, 2, 3, 4, 5]
sub_list = my_list[:] # 切片是个浅拷贝的操作
sub_list[0] = 10
print(my_list)
print(sub_list)
print(id(my_list[1]))
print(id(sub_list[1]))
# [1, 2, 3, 4, 5]
# [10, 2, 3, 4, 5]
# 140719128709592
# 140719128709592

my_list = [1, 2, 3, 4, 5]
sub_list = my_list[-6:6] # 越界只会取合法边界
print(sub_list)

my_list[:]
my_list[:2]
my_list[2:]

length = len(my_list)
print(length)  # 输出 5

exists = 3 in my_list  # 输出 True

my_list = [11, 2, 33, 14, 5]
my_list.sort()
print(my_list)

sorted_list = sorted(my_list)

my_list.reverse()

copied_list = my_list.copy() # shallow copy


## 列表推导式
new_list = [expression for item in iterable if condition]

squares = [x ** 2 for x in range(1, 6)]
print(squares)  # 输出 [1, 4, 9, 16, 25]

evens = [x for x in range(1, 11) if x % 2 == 0]
print(evens)  # 输出 [2, 4, 6, 8, 10]
evens = [x for x in range(1, 11) if x & 1 == 0]
print(evens)  # 输出 [2, 4, 6, 8, 10]

# 嵌套列表推导式
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat_list = [num for row in matrix for num in row]
print(flat_list)  # 输出 [1, 2, 3, 4, 5, 6, 7, 8, 9]
