def add(a, b):
    return a + b

plus = add

plus(3, 4)


## Lambda
(lambda a, b: a + b)(3, 4)  # returns 7

addition = lambda a, b: a + b
addition(3, 4)

authors = ['Octavia Butler', 'Isaac Asimov', 'Neal Stephenson', 'Margaret Atwood', 'Usula K Le Guin', 'Ray Bradbury']
sorted(authors, key=len)  # Returns list ordered by length of author name
sorted(authors, key=lambda name: name.split()[-1])


from functools import partial

def power(base, exp):
    return base ** exp

cube = partial(power, exp=3)
cube(5)

