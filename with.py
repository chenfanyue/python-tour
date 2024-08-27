# `with` safely deal with file
with open("data", "r") as file:
    content = file.read()
    print(content)

with open("data", "w") as file:
    file.write('lamp on the desktop')

with open("data", "a") as file: # create, read, write, append
    file.write('append mode')


# `with` used in exception
try:
    with open("example.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("文件未找到！")


# `with` and customed context
class MyContext:
    def __enter__(self):
        print("进入上下文")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("退出上下文")

with MyContext() as context:
    print("处理中...")


# yield 之前的代码在进入上下文时执行，yield 之后的代码在退出上下文时执行
from contextlib import contextmanager

@contextmanager
def my_context():
    print("进入上下文")
    yield
    print("退出上下文")

with my_context():
    print("处理中...")
