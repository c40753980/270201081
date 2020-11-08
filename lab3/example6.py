a = float(input('Enter the value of "a" : '))
b = float(input('Enter the value of "b" : '))
c = float(input('Enter the value of "c" : '))
d = b**2-4*a*c
if d < 0:
    print('no real roots')
elif d == 0:
    x = (-b) / 2*a
    print("x =", x)
else:
    x1 = (-b + d ** 0.5)/ 2*a
    x2 = (-b - d ** 0.5)/ 2*a

    print("x1 =", x1)
    print("x2 =", x2)
