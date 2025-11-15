ans = 0
for i in range(int(input())):
    a, b = map(int, input().split())
    temp = ans 
    temp -= a
    temp += b
    ans = max(ans, temp)
print(ans)