## 函数定义
def greet(name):
    print(f"Hello, {name}!")


## 参数传递
# 默认参数
def greet(name="World"):
    print(f"Hello, {name}!")

greet()         # 输出：Hello, World!
greet("Alice")  # 输出：Hello, Alice!

# 关键字参数
def greet(name, message):
    print(f"{message}, {name}!")

greet(name="Alice", message="Good morning")  # 输出：Good morning, Alice!
greet(message="Good morning", name="Alice")  # 输出：Good morning, Alice!

# 任意参数： 使用 *args 和 **kwargs 可以处理任意数量的位置参数和关键字参数
def greet(*names): # names tuple
    for name in names:
        print(f"Hello, {name}!")

greet("Alice", "Bob", "Charlie")  # 输出每个人的问候语

def greet(**kwargs): # kwargs dict
    for key, value in kwargs.items():
        print(f"{key}: {value}")

greet(name="Alice", message="Good morning")  # 输出键值对


## 作用域
x = 10  # 全局变量
print(id(x))

def func():
	# nonlocal 将变量绑定到外层函数的作用域
    global x
    print(id(x))
    x = 20  # 修改全局变量
    y = 30  # 局部变量

func()
print(x)  # 输出 20
# print(y)  # NameError: name 'y' is not defined


## 匿名函数 lambda
square = lambda x: x * x
print(square(5))  # 输出 25

# 定义一个 lambda 表达式，接受两个参数，返回它们的和
add = lambda x, y: x + y
# 调用 lambda 表达式
result = add(3, 5)
print(result)  # 输出: 8

# 使用 lambda 表达式和 map 函数，将两个列表中的元素逐对相加
numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]
sums = map(lambda x, y: x + y, numbers1, numbers2)
print(list(sums))  # 输出: [5, 7, 9]


## 高阶函数
# map 函数返回一个 map 对象，它是一个迭代器（iterator）
def square(x):
    return x * x

numbers = [1, 2, 3, 4, 5]
squares = map(square, numbers)
# map 对象是一个迭代器，因此可以将其转换为列表来查看结果
print(list(squares))  # 输出: [1, 4, 9, 16, 25]


# filter 函数也返回一个迭代器
def is_even(x):
    return x % 2 == 0

numbers = [1, 2, 3, 4, 5, 6]
even_numbers = filter(is_even, numbers)
# 将迭代器转换为列表来查看结果
print(list(even_numbers))  # 输出: [2, 4, 6]


# reduce
from functools import reduce

def add(x, y):
    return x + y

numbers = [1, 2, 3, 4, 5]
sum_of_numbers = reduce(add, numbers)
print(sum_of_numbers)  # 输出: 15


numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]
# 使用 zip 函数将两个列表组合成一个迭代器，生成 (x, y) 对
filtered_sums = filter(lambda pair: pair[0] + pair[1] > 5, zip(numbers1, numbers2))
# 只取出符合条件的原始列表的第一个元素
result = [x for x, _ in filtered_sums]
print(result)  # 输出: [2, 3]

numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]
result = [x for x, y in zip(numbers1, numbers2) if x+y > 5]
print(result)  # 输出: [2, 3]


def fibonacci(n, memo={}):
    if n <= 1:
        return n
    if n not in memo:
        memo[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return memo[n]

result = fibonacci(490)
print(result)
