x1, x2, x3 = map(int, input().split())
ans = 0
if x2 <= x1 <= x3 or x3 <= x1 <= x2:
    ans = abs(x2-x1)+abs(x3-x1)
elif x1 <= x2 <= x3 or x3 <= x2 <= x1:
    ans = abs(x1-x2)+abs(x3-x2)
else:
    ans = abs(x1-x3)+abs(x2-x3)
print(ans)