### Python 异常处理详解

#### 1. `try`, `except`, `finally` 的使用

在 Python 中，异常处理的核心机制是 `try`, `except`, 和 `finally` 语句块。它们用于捕获和处理运行时可能发生的异常，确保程序即使出现错误也能继续运行或优雅地退出。

**`try` 语句块**：用于包含可能会引发异常的代码。如果在 `try` 块中发生异常，解释器会立即停止执行剩余的代码，并转移到 `except` 块中。

**`except` 语句块**：用于捕获在 `try` 语句块中发生的特定异常。可以指定捕获一种或多种异常类型，并为每种异常提供不同的处理方式。

**`finally` 语句块**：无论是否发生异常，`finally` 块中的代码都会执行。它通常用于清理资源，例如关闭文件或释放锁。

**示例**：
```python
try:
    # 可能发生异常的代码
    result = 10 / 0
except ZeroDivisionError as e:
    # 处理特定异常
    print(f"捕获到异常：{e}")
finally:
    # 无论如何都会执行
    print("执行 finally 块")
```
在上述代码中，`try` 块中发生了 `ZeroDivisionError`，程序跳转到 `except` 块并打印异常信息。最后，无论是否发生异常，`finally` 块都会执行。

#### 2. 自定义异常类

Python 允许用户定义自己的异常类，以便在特定场景下使用。自定义异常类通常继承自内置的 `Exception` 类。

**示例**：
```python
class MyCustomError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

try:
    raise MyCustomError("这是一个自定义异常")
except MyCustomError as e:
    print(f"捕获到自定义异常：{e}")
```
在这个示例中，`MyCustomError` 是一个自定义异常类，当出现特定条件时，程序可以使用 `raise` 关键字手动引发该异常，并在 `except` 块中捕获和处理它。

#### 3. 常见的异常类型与处理

Python 提供了多种内置的异常类型，用于处理不同类型的错误。以下是一些常见的异常类型：

- **`IndexError`**: 当尝试访问列表、元组或其他序列中不存在的索引时引发。
- **`KeyError`**: 当尝试访问字典中不存在的键时引发。
- **`ValueError`**: 当函数接收到的参数类型正确但值不合适时引发。
- **`TypeError`**: 当操作或函数应用于不支持的类型时引发。
- **`FileNotFoundError`**: 当尝试打开不存在的文件时引发。
- **`IOError`**: 处理输入输出操作时发生的异常，例如文件无法打开。

**示例**：
```python
try:
    numbers = [1, 2, 3]
    print(numbers[3])
except IndexError as e:
    print(f"捕获到异常：{e}")
```
在这个示例中，尝试访问列表的索引 `3`，但列表中没有此索引，因此引发 `IndexError`，然后在 `except` 块中进行处理。

掌握异常处理的技巧有助于提高代码的鲁棒性和容错性，使程序能够在各种异常情况下正常运行或优雅退出。


```python
class MyCustomError(Exception):
    def __init__(self, message):
        super().__init__(message)

class MyCustomError(Exception):
    def __init__(self, message):
        self.message = message
```
这2中写法都可以运行，那有什么区别吗？

这两种写法在功能上可以正常运行，但它们有一些细微的区别，特别是在异常处理和属性访问方面。

### 1. 使用 `super().__init__(message)` 的方式

```python
class MyCustomError(Exception):
    def __init__(self, message):
        super().__init__(message)
```

这种写法调用了父类 `Exception` 的构造函数，并将 `message` 传递给它。这样做的好处是，`message` 会自动存储在异常实例的 `args` 属性中，并且异常对象会直接支持字符串表示。

- **自动处理字符串表示**: 当抛出异常时，异常消息会自动包含在异常的字符串表示中。例如，`str(e)` 会返回 `message` 的内容。

- **推荐的写法**: 这是推荐的写法，因为它遵循了 Python 的异常处理惯例，确保了异常消息能够正确传递和显示。

**示例**:
```python
try:
    raise MyCustomError("这是一个自定义异常")
except MyCustomError as e:
    print(str(e))  # 输出: 这是一个自定义异常
```

### 2. 使用 `self.message = message` 的方式

```python
class MyCustomError(Exception):
    def __init__(self, message):
        self.message = message
```

这种写法将 `message` 存储在自定义异常类的实例变量 `self.message` 中，但没有调用父类的构造函数。这意味着:

- **自定义存储属性**: 你可以直接访问 `self.message` 来获取异常消息。

- **字符串表示需要额外处理**: `str(e)` 不会自动返回 `message` 的内容，除非你重写了 `__str__` 或 `__repr__` 方法。如果你没有重写，`str(e)` 会返回一个空字符串或者默认的异常表示。

**示例**:
```python
try:
    raise MyCustomError("这是一个自定义异常")
except MyCustomError as e:
    print(str(e))  # 输出: 空字符串
    print(e.message)  # 输出: 这是一个自定义异常
```

### 总结

- **第一种方法** (`super().__init__(message)`): 使得异常对象的字符串表示自动包含异常消息，是更符合 Python 异常处理惯例的写法。

- **第二种方法** (`self.message = message`): 手动存储异常消息在 `self.message` 中，灵活性更高，但需要手动处理异常对象的字符串表示。

如果你的主要需求是让异常消息能够直接通过 `str(e)` 显示，那么推荐使用第一种方式。如果你需要对异常消息进行更细粒度的控制，可以选择第二种方式，但要注意可能需要额外处理字符串表示。