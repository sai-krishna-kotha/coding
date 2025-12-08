n = int(input())

ans_x = ans_y = None

for y in range(n // 7, -1, -1):
    rem = n - 7 * y
    if rem >= 0 and rem % 4 == 0:
        x = rem // 4
        ans_x, ans_y = x, y
        break

if ans_x is None:
    print(-1)
else:
    print("4" * ans_x + "7" * ans_y)
