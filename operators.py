# 算术运算符
15 / 3 == 5.0
11 // 3 == 3
11 % 3 == 2
2 ** 3 == 8

# 比较运算符

# 逻辑运算符
and # 短路操作 遇到False后面短路
or  # 短路操作 遇到True后面短路
not

# 位运算符
& | ^ ~ << >>

def is_even(number):
    return (number & 1) == 0

# *iterable
print(*[1, 2, 3])
