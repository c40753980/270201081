student=int(input("Enter the number of students : "))
average_grades=[]


for i in range(student):
  midterm1=int(input("Enter the grade of Student"+str(i+1)+" midterm 1 : "))
  midterm2=int(input("Enter the grade of Student"+str(i+1)+" midterm 2 : "))
  final=int(input("Enter the grade of Student"+str(i+1)+" final : "))
  
  while midterm1>100 or midterm2>100 or final>100:
    print("Invalid Grade Try Again !")
    midterm1=int(input("Enter the grade of Student"+str(i+1)+" midterm 1 : "))
    midterm2=int(input("Enter the grade of Student"+str(i+1)+" midterm 2 : "))
    final=int(input("Enter the grade of Student"+str(i+1)+" final : "))


  g=(midterm1*0.3)+(midterm2*0.3)+(final*0.4)
  if g>=90:
    average_grades.append([g])
  
if average_grades==[]:
    print('Sorry! There is no any "AA" grade :( ')
else:
    print(average_grades)