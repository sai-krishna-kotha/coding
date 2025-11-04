n = int(input())
arr = input()
ans = 0
for i in range(1, n):
    if arr[i] == arr[i-1]:
        ans += 1
print(ans)