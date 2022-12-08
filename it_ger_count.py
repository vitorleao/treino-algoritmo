# Exercise 1
# print the integer 2 through 10 using a "for" loop
for i in range(2, 11):
    print(i)


# Exercise 2
# print the integer 2 through 10 using a "while" loop
i = 2
while i < 11:
    print(i)
    i = i + 1


# Exercise 3
def doubles(num):
    """Return the result of multiplying an input number by 2."""
    return num * 2


# Call doubles() to double the number 2 three times
my_num = 2
for i in range(0, 3):
    my_num = doubles(my_num)
    print(my_num)

l1 = [x for x in range(3)]
l2 = (x for x in range(3))

for v in l1:
    print(v)

for u in l2:
    print(u)

cart = []
cart.append(('P1', 10))
cart.append(('P2', '20'))
cart.append(('P3', 30))

total = sum([float(y) for x, y in cart])
print(total)

from itertools import count
cont = count(start=-1, step=-1)

for value in cont:
    print(round(value, 2))

    if value >= 3 or value <= -3:
        break