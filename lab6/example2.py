student=int(input("Enter the number of students : "))
average_grades=[]

for i in range(student):
  midterm1=int(input("Enter the grade of Student"+str(i+1)+" midterm 1 : "))
  midterm2=int(input("Enter the grade of Student"+str(i+1)+" midterm 2 : "))
  final=int(input("Enter the grade of Student"+str(i+1)+" final : "))

  average_grades.append([((midterm1*0.3)+(midterm2*0.3)+(final*0.4))])


print(average_grades)
