a= int(input("Enter : "))
n=int(input("Enter :"))
if n<=0:
  print("Invalid !")
elif n>10:
  print("Less than 10 !")
else:
    for i in range(1,n+1):
      print(str(a)+"*"+str(i)+"="+str(a*i))
       