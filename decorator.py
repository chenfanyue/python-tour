## 函数装饰器
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Function is being called.")
        result = func(*args, **kwargs)
        print("Function has been called.")
        return result
    return wrapper

@my_decorator
def say(name):
    print(f'hi {name}')

say('alice')
# Function is being called.
# hi alice
# Function has been called.


## 函数装饰器的应用场景
# 1. 权限检查装饰器
def check_permission(role_required): # 装饰器工厂
    def decorator(func): # 装饰器
        def wrapper(user_role, *args, **kwargs): # 包装函数
            if user_role == role_required:
                return func(*args, **kwargs)
            else:
                print("Access denied.")
        return wrapper
    return decorator

@check_permission("admin")
def delete_data():
    print("Data deleted.")

# 示例
user_role = "admin"
delete_data(user_role)  # 输出: Data deleted.

user_role = "guest"
delete_data(user_role)  # 输出: Access denied.


# 2. 日志记录装饰器
def log_function_call(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function {func.__name__} with args: {args} and kwargs: {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@log_function_call
def add(a, b):
    return a + b

# 示例
result = add(2, 3)  # 输出: Calling function add with args: (2, 3) and kwargs: {}
print(result)       # 输出: 5


# 3. 缓存装饰器
def cache(func):
    cache_storage = {}

    def wrapper(*args):
        print(args)
        if args not in cache_storage:
            print('update cache storage')
            result = func(*args)
            cache_storage[args] = result
        return cache_storage[args]

    return wrapper

@cache
def expensive_computation(x):
    print(f"Expensive Computing {x}...")
    return x * x

print(expensive_computation(10))
print(expensive_computation(10))


# 4. 性能监控装饰器
import time

def performance_monitor(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function {func.__name__} took {end_time - start_time:.6f} seconds")
        return result
    return wrapper

@performance_monitor
def slow_function():
    time.sleep(10)
    print("Function complete")

# 示例
slow_function()  # 输出: Function complete \n Function slow_function took 2.000xxx seconds


## 类装饰器
def my_class_decorator(cls):
    class Wrapper(cls):
        def new_method(self):
            print("New method added by decorator.")
        # 可以在这里重写类的方法或属性
    return Wrapper

@my_class_decorator
class MyClass:
    def original_method(self):
        print("Original method.")

obj = MyClass()
obj.original_method()
obj.new_method()
# Original method.
# New method added by decorator.


## fibonacci with decorator
def cache(func):
    cache_storage = {}

    def wrapper(*args):
        if args not in cache_storage:
            result = func(*args)
            cache_storage[args] = result
        return cache_storage[args]

    return wrapper

@cache
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(490))
