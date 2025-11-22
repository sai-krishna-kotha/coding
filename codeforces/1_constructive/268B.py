n = int(input())
ans = 0
def summ(i):
    ans = 0
    for i in range(1, i+1):
        ans += i
    return ans
if n == 1:
    print(1)
else:
    for i in range(n, 1, -1):
        if i == 2:
            ans += i + 1
        else:
            ans += i + summ(i-2)
    print(ans)