n = int(input())
def sum_n(n: int):
    return n*(n+1)/2
ans = 0
temp = 0
while temp < n:
    ans += 1
    temp += sum_n(ans)
    if temp > n:
        print(ans-1)
        break
    if temp == n:
        print(ans)

