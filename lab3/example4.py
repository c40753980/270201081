age = int(input("Enter your age :"))
normal_price = 3
if age>60 or age<6:
  print("Your ticket is free")
elif age>6 and age<18:
  normal_price1 = normal_price * 0.5
  print("Your ticket price is " , normal_price1)
else:
  print("Your ticket price is ", normal_price)