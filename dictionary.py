empty_dict = {}

student = {
    "name": "Alice",
    "age": 20,
    "major": "Computer Science"
}

student = dict(
    name="Alice",
    age=20,
    major="Computer Science",
)

student = dict(name="Alice", age=20, major="Computer Science")

items = [("name", "Alice"), ("age", 20), ("major", "Computer Science")]
student = dict(items)

items = [["name", "Alice"], ["age", 20], ["major", "Computer Science"]]
student = dict(items)

items = (("name", "Alice"), ("age", 20), ("major", "Computer Science"))
student = dict(items)

items = (["name", "Alice"], ["age", 20], ["major", "Computer Science"])
student = dict(items)


name = student["name"]  # 获取 "name" 键对应的值

gpa = student.get("gpa", "N/A")  # 如果 "gpa" 不存在，返回 "N/A"


if 'name' in student:
    pass

if 'unknown' not in student:
    pass
