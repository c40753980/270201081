number=int(input('Enter the number : '))
a=number%100
if 0<=a<10:
  print('0'+ str(a))
else:
  print(a)
