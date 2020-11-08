a=int(input('Enter number 1 : '))
b=int(input('Enter number 2 : '))
c=int(input('Enter number 3 : '))

if a>b>c or b>a>c:
  print('Minimum is ',c)
elif b>c>a or c>b>a :
  print('Minimum is',a)
elif a>c>b or c>a>b:
  print('Minimum is',b)