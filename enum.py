from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

print(Color.GREEN)
print(Color['GREEN'])
print(Color(2))
print(Color.GREEN.name)
print(Color.GREEN.value)
print(Color.GREEN == Color.GREEN)
print(Color.GREEN is Color.GREEN)
print(len(Color))
print(list(Color))

for color in Color:
    print(color)


###
from enum import Enum, auto

class Animal(Enum):
    DOG = 1
    CAT = 10
    BIRD = auto()


print(list(Animal))
# [<Animal.DOG: 1>, <Animal.CAT: 10>, <Animal.BIRD: 11>]


class Status(Enum):
    SUCCESS = 1
    FAILURE = 2
    OK = 1  # Alias for SUCCESS


# Flag Enums: You can use bitwise flags for more complex states.
# Use Flag or IntFlag for bitmask-style enums
from enum import Flag, auto

class Permissions(Flag):
    READ = auto()
    WRITE = auto()
    EXECUTE = auto()

print(list(Permissions))
