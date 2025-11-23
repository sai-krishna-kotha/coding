n, m = map(int, input().split())
half = n//2 + (n % 2 != 0)
if n < m:
    print(-1)
else:
    if half % m == 0:
        print(half)
    else:
        cnt = 0
        for i in range(half+1, half+m+1):
            cnt += 1
            if i % m == 0:
                break
        print(half+cnt)