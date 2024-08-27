## 类方法 常见用途是作为工厂方法，用于创建类的不同实例
class MyClass:
    class_attribute = "I am a class attribute"

    def __init__(self, value):
        self.value = value

    @classmethod
    def create_instance(cls, value):
        return cls(value)

    @classmethod
    def show_class_attribute(cls):
        print(cls.class_attribute)

# 使用类方法创建实例
instance = MyClass.create_instance(10)
print(instance.value)  # 输出: 10

# 调用类方法访问类属性
MyClass.show_class_attribute()  # 输出: I am a class attribute


# 工厂模式的实现
class Vehicle:
    def __init__(self, name):
        self.name = name

    @classmethod
    def create_vehicle(cls, type, name):
        if type == 'car':
            return Car(name)
        elif type == 'bike':
            return Bike(name)
        else:
            return cls(name)

class Car(Vehicle):
    def __init__(self, name):
        super().__init__(name)

class Bike(Vehicle):
    def __init__(self, name):
        super().__init__(name)

# 使用类方法创建不同类型的车辆
car = Vehicle.create_vehicle('car', 'Sedan')
bike = Vehicle.create_vehicle('bike', 'Mountain Bike')
vehicle = Vehicle.create_vehicle('unknown', 'Generic Vehicle')

print(type(car))    # 输出: <class '__main__.Car'>
print(type(bike))   # 输出: <class '__main__.Bike'>
print(type(vehicle))# 输出: <class '__main__.Vehicle'>



# 参数验证、对象缓存、甚至返回已有实例
class MyClass:
    _instances = {} # 缓存机制

    def __init__(self, value):
        self.value = value

    @classmethod
    def create_instance(cls, value):
        if value not in cls._instances:
            cls._instances[value] = cls(value)
        return cls._instances[value]

# 通过类方法保证相同参数只创建一个实例
instance1 = MyClass.create_instance(10)
instance2 = MyClass.create_instance(10)

print(instance1 is instance2)  # 输出: True


# 继承中的优势
class Base:
    def __init__(self, value):
        self.value = value

    @classmethod
    def create_instance(cls, value):
        return cls(value)

class Derived(Base):
    def __init__(self, value):
        super().__init__(value)
        self.extra = value * 2

# 调用子类的类方法创建实例
derived_instance = Derived.create_instance(5)
print(type(derived_instance))  # 输出: <class '__main__.Derived'>
print(derived_instance.extra)  # 输出: 10



## 静态方法
class MyClass:

    @staticmethod
    def add_numbers(a, b):
        return a + b

# 使用类名调用静态方法
result = MyClass.add_numbers(5, 10)
print(result)  # 输出: 15

# 也可以通过实例调用静态方法
instance = MyClass()
result = instance.add_numbers(3, 7)
print(result)  # 输出: 10
