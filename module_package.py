## 导入内置模块
import math

result = math.sqrt(16)
print(result)  # 输出: 4.0


from math import sqrt

result = sqrt(16)
print(result)  # 输出: 4.0


from math import sqrt as sqt

result = sqt(16)
print(result)  # 输出: 4.0


from math import sqrt, pow

result = sqrt(16)
power = pow(2, 3)
print(result)  # 输出: 4.0
print(power)   # 输出: 8.0


## 自定义模块
# 创建自定义模块
# mymath.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

# 导入自定义模块
# main.py
import mymath

result1 = mymath.add(5, 3)
result2 = mymath.subtract(5, 3)

print(result1)  # 输出: 8
print(result2)  # 输出: 2

# 也可以使用 from ... import ... 语法导入特定的函数
from mymath import add

result = add(5, 3)
print(result)  # 输出: 8


## package
# 创建包
/**
my_package/
    __init__.py
    module1.py
    module2.py
*/

# module1.py
def func1():
    print("This is function 1 from module 1")

# module2.py
def func2():
    print("This is function 2 from module 2")

# 导入包中的模块
# main.py
from my_package import module1, module2

module1.func1()  # 输出: This is function 1 from module 1
module2.func2()  # 输出: This is function 2 from module 2

# __init__.py 文件可以用来控制从包中导入内容
# __init__.py
from .module1 import func1
from .module2 import func2

# main.py
from my_package import func1, func2

func1()  # 输出: This is function 1 from module 1
func2()  # 输出: This is function 2 from module 2
