name = input("请输入您的名字: ")
age = int(input("请输入您的年龄: "))
print(f"你好, {name}! 您的年龄是 {age} 岁。")


name = "Alice"
score = 95.5
print(f"{name + 'girl'}的成绩是: {score+1:.2f} 分")


# str.format()
# 学生信息
name = "张三"
math_score = 88
english_score = 92
science_score = 79

# 使用 str.format() 格式化输出成绩单
report_card = "学生: {}\n数学: {}\n英语: {}\n科学: {}".format(name, math_score, english_score, science_score)

# 也可以指定占位符中的位置参数
report_card = "学生: {0}\n数学: {1}\n英语: {2}\n科学: {3}".format(name, math_score, english_score, science_score)

# 或者使用命名参数
report_card = "学生: {name}\n数学: {math}\n英语: {english}\n科学: {science}".format(
    name=name, math=math_score, english=english_score, science=science_score)

# 或者通过字符串插值
report_card = f"学生: {name}\n数学: {math_score}\n英语: {english_score}\n科学: {science_score}"

# 打印成绩单
print(report_card)
