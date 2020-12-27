employees = {}
for i in range(1,6):
  name = input('enter name: ')
  salary= int(input('enter salary: '))
  employees[name] = salary

sorted_employees = sorted(employees.items(), key=lambda x: x[1], reverse=False)
for i in range(len(sorted_employees)):
    if i>1:
        print(sorted_employees[i])