def hailstone(x):
   a = str(x)

   if x == 1:
     return a
   elif x%2 == 0:
     return str(x) + ';' + hailstone(x//2)
   else:
     return str(x) + ';' + hailstone((3*x)+1)

print(hailstone(5))
