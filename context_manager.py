##
在 Python 中，上下文管理器是一种用于管理资源的工具，常见的应用场景包括文件操作、网络连接、数据库连接等。在上下文管理器中，我们通常使用 with 语句来确保资源的正确分配和释放。上下文管理器的核心在于它实现了两个特殊方法：__enter__ 和 __exit__。通过自定义上下文管理器，你可以精确控制资源的初始化和清理过程


## 自定义上下文管理器
class MyContextManager:
    def __enter__(self):
        print("进入上下文，资源初始化")
        return "资源已经准备好"

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            print(f"捕获到异常：{exc_type}: {exc_value}")
        print("退出上下文，资源清理")
        return True  # 如果你希望 suppress（抑制）异常，返回 True，否则返回 False 或 None

with MyContextManager() as resource:
    print(resource)
    raise ValueError('值错误')


## 实际应用
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            self.file.close()
        if exc_type:
            print(f"文件操作时发生异常：{exc_value}")
        return False  # 不抑制异常，异常会继续向上传递

# 使用 FileManager 管理文件读写
with FileManager('example.txt', 'a') as file:
    file.write("some text from FileManager\n")
