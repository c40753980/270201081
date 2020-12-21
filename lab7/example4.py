name_list = []
salary_list = []
employees = {}


for i in range(5):
  name = str(input('Name: '))
  salary = int(input('Salary: '))

  name_list.append(name)
  salary_list.append(salary)

for x,y in zip(name_list,salary_list):
  employees[x] = y

sorted_salary = sorted(employees.values())

for a in sorted_salary:

  for b in employees.keys():

    if employees[b] == a:
      print(b[2],b[3],b[4])
      print(employees[b[2],b[3],b[4]])