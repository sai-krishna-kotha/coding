from math import ceil
for i in range(int(input())):
    n = int(input())
    print(2)
    curr = n
    for i in range(n-1, 0, -1):
        print(curr, i)
        curr = ceil((i+curr)/2)