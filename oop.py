class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} is barking!"

    def get_age(self):
        return f"{self.name} is {self.age} years old."

# 创建对象
my_dog = Dog(name="Buddy", age=3)

# 调用实例方法
print(my_dog.bark())       # 输出: Buddy is barking!
print(my_dog.get_age())    # 输出: Buddy is 3 years old.


# 单继承
from typing import override
class Animal:
    def speak(self):
        return "Some sound"

class Dog(Animal):
    @override
    def speak(self):
        return "Woof!"

# 多继承
class Walker:
    def walk(self):
        return "Walking"

class Swimmer:
    def swim(self):
        return "Swimming"

class Amphibian(Walker, Swimmer):
    pass


# override
class Animal:
    def speak(self):
        return "Some sound"

class Bird(Animal):
    def speak(self):
        parent_sound = super().speak()
        return f"{parent_sound} and chirp!"


## magic methods
# __str__ “可读”字符串表示
class MyClass:
    pass

obj = MyClass()
print(obj)  # 输出: <__main__.MyClass object at 0x0000015EFCA315E0>

class MyClass:
    def __str__(self):
        return "This is MyClass instance"

obj = MyClass()
print(obj)  # 输出: This is MyClass instance
# print(str(obj))  # 输出: This is MyClass instance


# __repr__ 序列化表示？
class MyClass:
    def __repr__(self):
        return "MyClass()"

obj = MyClass()
print(repr(obj))  # 输出: MyClass()


# __add__
class MyNumber:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return MyNumber(self.value + other.value)

    def __repr__(self):
        return f"MyNumber({self.value})"

num1 = MyNumber(10)
num2 = MyNumber(20)
print(num1 + num2)  # 输出: MyNumber(30)


/**
__sub__(self, other)：定义减法运算（-）。
__mul__(self, other)：定义乘法运算（*）。
__truediv__(self, other)：定义除法运算（/）。
__eq__(self, other)：定义等于运算符（==）。
__lt__(self, other)：定义小于运算符（<）。
__len__(self)：定义len()函数的行为。
__getitem__(self, key)：定义索引操作的行为，如obj[key]。
__setitem__(self, key, value)：定义赋值操作的行为，如obj[key] = value
*/
