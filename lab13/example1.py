def selection_sort(n):

    for i in range(len(n)-1):

        min_ = i

        for j in range(i+1, len(n)-1):
            if n[j] < n[min_]:
                min_ = j

        n[i], n[min_] = n[min_], n[i]


n = [3, 1, 41, 59, 26, 53, 59]
selection_sort(n)
print(n)