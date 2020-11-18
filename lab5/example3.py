a=int(input("Enter number 1 : "))
b=int(input("Enter number 2 : "))
n=0

while a>0 and b>0:
  if a%10==b%10:
    n+=1
  
  a= a//10
  b= b//10

print(n)
 