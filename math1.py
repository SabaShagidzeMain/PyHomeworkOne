import math as m

x = int(input("write X"))
y = int(input("write Y"))
z = int(input("write Z"))

if y <= x < 0 and z != 0:
    z = round((m.sqrt(x-y))/z)
elif y > x > 0 and z != 0:
    z = round(m.sqrt(y-x)/z)
else:
    z = "X and Z can't be equal to zero!"

print(z)
