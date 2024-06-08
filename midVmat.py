import statistics
a = [[1,2,3],[4,5,6],[7,8,9]]
lists = []
for row in range(len(a)):
    for column in range(len(a[0])):
        lists.append(a[row][column])
if len(lists)%2 ==0:
    print("Null")
else:
    print("The mid value is:",statistics.median(lists))

