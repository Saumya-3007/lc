from itertools import chain
a = [[1,2,3],[4,5,6],[7,8,9]]
lists = []
for row in range(len(a)):
    for column in range(len(a[0])):
        lists.append(a[row][column])
print(f"Max:{max(lists)}")
print(f"Min:{min(lists)}")


a = [[1,2,3],[4,5,6],[7,8,9]]
n = [a[row][column] for row in range(len(a)) for column in range(len(a[0]))]
print(max(n))
print(min(n))

