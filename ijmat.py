a = [[1,0],[0,5],[7,8]]
i= []
j =[]
for row in range(len(a)):
    for column in range(len(a[0])):
        j.append(column)
    i.append(row)
print(f"This is {max(i)+1} * {max(j)+1} matrix")