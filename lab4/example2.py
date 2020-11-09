year=int(input('Enter the year : '))
if (year%100==0 and year%400==0):
  print("Leap Year")
else:
  print("Not Leap Year")