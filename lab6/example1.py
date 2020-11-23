email=input("Enter the email : ")
x= "ceng113@example.com"

email=email.lower()

index=email.index("@")
before_email=email[0:index]
after_email=email[index:]

before_email = before_email.replace("","")
email = before_email + after_email

if email==x:
  print("Correct! ")
else:
  print("Wrong!")