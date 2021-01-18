def selection_sort(n):

    for i in range(len(n)-1):

        min_ = i

        for j in range(i+1, len(n)-1):
            if n[j] < n[min_]:
                min_ = j

        n[i], n[min_] = n[min_], n[i]


n = [22, 8, 12, -4, 27, 30, 36, 50, 7, 68, 91, 56, 2, 85, 42, 98, 25]
selection_sort(n)
print(n)