/**
元组的特性

不可变性:
元组是不可变的数据结构，一旦创建，元组中的元素不能被修改、添加或删除。这使得元组在需要保护数据不被意外更改时非常有用。这与列表（list）的可变性形成了对比。

有序性:
元组中的元素是有序的，可以通过索引访问每一个元素。元组的元素可以是任意类型，包括其他元组、列表、字典等复合类型。

多样性:
元组可以包含多种数据类型。例如，一个元组可以同时包含整数、字符串和浮点数。这使得元组非常灵活，能够用于存储各种类型的数据。

轻量性:
由于元组是不可变的，因此它们通常比列表更为轻量，且内存占用更少。这使得元组在需要频繁读取数据且不需要修改数据的情况下成为高效的选择。

解包（Unpacking）:
元组支持解包操作，即可以将元组中的元素直接赋值给多个变量。例如：
point = (3, 4)
x, y = point

哈希性:
由于元组是不可变的，因此它们是可哈希的，可以作为字典的键或存储在集合中
*/

def get_coordinates():
    return (10, 20)
x, y = get_coordinates()

coordinates = {}
coordinates[(10, 20)] = "Location A"

(year, month, day)

a, b = b, a
