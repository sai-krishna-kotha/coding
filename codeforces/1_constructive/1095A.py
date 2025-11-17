n = int(input())
string = input()
def sum_n(n):
    return n*(n+1)//2
i = 1
idx = 0
ans = ''
while idx < n:
    idx = sum_n(i)
    ans += string[idx-1]
    i += 1
print(ans)