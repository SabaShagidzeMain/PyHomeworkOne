import math as m

x = int(input("Write X"))
y = int(input("Write Y"))
z = int(input("Write Z"))

if x != y or x != z and z > 0:
    f = (m.pow(x, y)/z)
elif x == y or x == z and z > 0:
    f = m.pow((x*y), y)/z
else:
    f = "not defined"
print(f)
