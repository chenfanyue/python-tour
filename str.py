print(list(b'bytes object'))
# [98, 121, 116, 101, 115, 32, 111, 98, 106, 101, 99, 116]

print(list('bytes object'))
# ['b', 'y', 't', 'e', 's', ' ', 'o', 'b', 'j', 'e', 'c', 't']

# 字符串大小写转换
str.upper()
str.lower()
str.capitalize()
str.title()

str.strip() # trim function in other languages
str.lstrip()
str.rstrip()

text = "hello world"
print(text.find("world"))  # 输出：6
print(text.replace("world", "Python"))  # 输出：hello Python
print(text) # 输出：hello world

str.split(sep)
text = "hello world"
words = text.split(" ")
print(words)  # 输出：['hello', 'world']

sep.join(iterable)
joined_text = '#'.join(words)
print(joined_text)  # 输出：hello#world

# f-string
name = "Alice"
age = 30
greeting = f"Hello, {name}. You are {age} years old."
print(greeting)  # 输出：Hello, Alice. You are 30 years old.

result = f"The sum of 2 and 3 is {2 + 3}."
print(result)  # 输出：The sum of 2 and 3 is 5.

pi = 3.14159
formatted_pi = f"Pi to three decimal places: {pi:.3f}"
print(formatted_pi)  # 输出：Pi to three decimal places: 3.142
