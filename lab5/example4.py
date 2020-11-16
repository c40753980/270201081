passw="abc123"
enter=input("Enter your password : ")


    
while passw!=enter:
  print("Wrong !")
  enter=input("Enter your password : ")
  if enter=="help":
    print(passw[0])
    enter=input("Enter your password : ")
  elif enter==passw:
    break
print("Welcome!")
    
  
