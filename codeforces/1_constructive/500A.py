n, t = map(int, input().split())
arr = list(map(int, input().split()))
i = 1
while i < t:
    i = i + arr[i-1]
if i == t:
    print("YES")
else:
    print("NO")