import math as m

a = int(input("Write A"))
b = int(input("Write B"))
c = int(input("Write C"))
d = int(input("Write D"))

if a > b and a > c and d != 0:
    z = round(m.sqrt(((a-b)*c)/m.pow(d, a)))
    print(z)
elif a < b and a < c or d == 0:
    z = ((a+b)*(c-a))*(d+a)
    print(z)
elif a == b and a != c and d != 0:
    z = ((a*b)/c)*d
    print(z)
else:
    print("error")
