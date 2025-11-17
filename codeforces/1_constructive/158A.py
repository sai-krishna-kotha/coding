n, k = map(int, input().split())
arr = list(map(int, input().split()))
x = arr[k-1]
ans = 0
for i in range(n):
    if arr[i] > 0 and arr[i] >= x:
        ans += 1
print(ans)