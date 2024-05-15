
def find_combinations(n, path=[]):
    if n == 0:
        result = "+".join(map(str, path))
        print(f"{result}")
    elif n < 0:
        return
    else:
        find_combinations(n-1, path + [1])
        find_combinations(n-2, path + [2])


n = int(input("Enter the num: "))
find_combinations(n)


