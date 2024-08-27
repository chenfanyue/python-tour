import copy

original = [1, 2, [3, 4]]
shallow_copied = copy.copy(original)
print(id(original[0]), id(shallow_copied[0]), sep='\n')

shallow_copied[0] = 11
print(id(original[0]), id(shallow_copied[0]), sep='\n')

shallow_copied[2].append(5)
print(original)  # 输出: [1, 2, [3, 4, 5]]
print(shallow_copied)  # 输出: [11, 2, [3, 4, 5]]
