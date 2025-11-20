n, m = map(int, input().split())
if m % n == 0:
    ans = 0
    d = m/n
    while d % 2 == 0:
        d //= 2
        ans += 1
    while d % 3 == 0:
        d //= 3
        ans += 1
    if d != 1:
        print(-1)
    else:
        print(ans)
else:
    print(-1)