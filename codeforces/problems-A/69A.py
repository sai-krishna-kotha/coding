n = int(input())
a =b=c=0
for _ in range(n):
    x, y, z = map(int, input().split())
    a += x
    b += y
    c += z
if a != 0 or b != 0 or c != 0:
    print("NO")
else:
    print("YES")