for i in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    print(abs(arr[n]-arr[n-1]))