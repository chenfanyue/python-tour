##
import time

start_time = time.time()

# 你的代码块
for i in range(1000000):
    pass

end_time = time.time()
elapsed_time = end_time - start_time

print(f"代码块执行时间: {elapsed_time} 秒")


## timeit 模块专门用于测量小段代码的执行时间，尤其是适合用于基准测试
import timeit

def code_to_test():
    for i in range(1000000):
        pass

elapsed_time = timeit.timeit(code_to_test, number=1)
print(f"代码块执行时间: {elapsed_time} 秒")


## contextmanager
import time
from contextlib import contextmanager

@contextmanager
def timer():
    start_time = time.time()
    yield
    end_time = time.time()
    print(f"代码块执行时间: {end_time - start_time} 秒")

with timer():
    # 你的代码块
    for i in range(1000000):
        pass


## datetime
from datetime import datetime

start_time = datetime.now()

# 你的代码块
for i in range(1000000):
    pass

end_time = datetime.now()
elapsed_time = end_time - start_time

print(f"代码块执行时间: {elapsed_time.total_seconds()} 秒")


## perf_counter
import time

start_time = time.perf_counter()

# 你的代码块
for i in range(1000000):
    pass

end_time = time.perf_counter()
elapsed_time = end_time - start_time

print(f"代码块执行时间: {elapsed_time} 秒")
