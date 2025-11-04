n, h = map(int, input().split())
heights = list(map(int, input().split()))
ans = 0
for ele in heights:
    if ele <= h:
        ans += 1
    else:
        ans += 2
print(ans)