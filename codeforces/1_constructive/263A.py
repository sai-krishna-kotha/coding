for i in range(1,6):
    j = 1
    for k in list(map(int, input().split())):
        if k == 1:
            print(abs(i-3)+abs(j-3))
        j += 1
        