numbers = int(input("How many numbers ? : "))
even = 0
for i in range(numbers):
  a = int(input("Enter an integer : "))
  if a % 2 == 0:
    even += 1
# now we have to convert integer to the %
even =(even/numbers)*100

print(str(even) + "%")
  

  
