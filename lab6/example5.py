n = int(input("Enter the size of Identity Matrix : "))
for row in range(0,n):
  for col in range(0,n):
    if (row == col):
      print("1 ",end=" ")
    else:
      print("0 ",end=" ")
   print()