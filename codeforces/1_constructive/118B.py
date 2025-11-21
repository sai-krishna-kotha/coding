n = int(input())
for i in range(2*n+1):
    if i <= n:
        for j in range(n-i):
            print(" ", end=" ")
        for j in range(i+1):
            if j == 0 and j == i:
                print(f"{j}", end="")
            else:
                print(f"{j}", end=" ")
        for j in range(i-1, -1, -1):
            if j == 0:
                print(f"{j}", end="")
            else:
                print(f"{j}", end=" ")
        print()
    else:
        i = i - n
        for j in range(i):
            print(" ", end=" ")
        for j in range(n-i+1):
            if j == 0 and j == n-i:
                print(f"{j}", end="")
            else:
                print(f"{j}", end=" ")
        for j in range(n-i-1,-1,-1):
            if j == 0:
                print(f"{j}", end="")
            else:
                print(f"{j}", end=" ")
        print()