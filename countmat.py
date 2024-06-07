from collections import Counter
a = [[1,0,3],[0,5,6],[7,8,9]]
lists = []
b = []
for row in range(len(a)):
    for column in range(len(a[0])):
        lists.append(a[row][column])
for x in lists:
    if x > 0:
        b.append(x)
print(len(b))






a = [[1,0,3],[0,5,6],[7,8,9]]
lists = [a[row][column] for row in range(len(a)) for column in range(len(a[0]))]
b = [x for x in lists if x > 0]
print(len(b))





