ans = 0
temp = 0
for i in range(int(input())):
    a, b = map(int, input().split())
    temp += (b-a)
    ans = max(ans, temp)
print(ans)