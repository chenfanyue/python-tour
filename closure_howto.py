## 闭包函数
/**
要创建闭包函数，通常需要三个步骤：
定义一个外部函数，其中包含局部变量。
在外部函数内部定义一个内层函数，内层函数可以使用外部函数的局部变量。
返回内层函数，使得内层函数可以在外部函数之外调用，同时“记住”外部函数的变量
*/

# 数据隐藏
def create_account(initial_balance):
    balance = initial_balance  # 这是一个隐藏的数据

    def __get_balance():
        return balance  # 只暴露查看余额的功能

    def __deposit(amount):
        nonlocal balance
        balance += amount  # 更新隐藏的数据

    def __withdraw(amount):
        nonlocal balance
        if amount <= balance:
            balance -= amount
            return True
        else:
            return False

    return __get_balance, __deposit, __withdraw

# 创建一个账户，初始余额为1000
get_balance, deposit, withdraw = create_account(1000)

# 查看余额
print(get_balance())  # 输出: 1000

# 存款
deposit(500)
print(get_balance())  # 输出: 1500

# 取款
withdraw(200)
print(get_balance())  # 输出: 1300

# 外部代码无法直接访问余额变量
# print(balance)  # 会抛出 NameError，因为 balance 在外部不可见


# 延迟计算
def delayed_execution(x, y):
    def compute():
        return x + y  # 仅在调用 compute 时才执行加法运算

    return compute

# 创建一个延迟计算的闭包
delayed_sum = delayed_execution(3, 5)

# 此时计算还未执行
# 执行计算
print(delayed_sum())  # 输出: 8


# 状态记忆
def make_counter():
    count = 0  # 初始化状态

    def counter():
        nonlocal count  # 使用并更新外部的状态
        count += 1
        return count

    return counter

# 创建一个计数器
counterA = make_counter()

# 每次调用计数器时，状态 count 都会被记住并递增
print(counterA())  # 输出: 1
print(counterA())  # 输出: 2
print(counterA())  # 输出: 3

# 创建另一个独立的计数器
counterB = make_counter()
print(counterB())  # 输出: 1
print(counterB())  # 输出: 2
