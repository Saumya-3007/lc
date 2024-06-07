a = [[1,2,3], [4,5,6],[7,8,9]]
b = [[1,2,3],[4,5,6],[7,8,9]]
res = [[0,0,0],[0,0,0],[0,0,0]]
for row in range(len(a)):
    for column in range(len(a[0])):
        res[row][column] = a[row][column] + b[row][column]
for r in res:
    print(r)





