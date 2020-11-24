n = list(map(int,input("Enter your list : ").split(' ')))
unique_list = []

for x in n:
    if x not in unique_list:
      unique_list.append(x)

#bubblesort
for i in range(len(unique_list)):
        for j in range(len(unique_list)-1):
            if unique_list[j] > unique_list[j+1]:
                c =  unique_list[j]
                unique_list[j] = unique_list[j+1]
                unique_list[j+1] = c

print(unique_list)