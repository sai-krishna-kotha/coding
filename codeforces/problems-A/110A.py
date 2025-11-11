n = int(input())
other = False
cnt = 0
def lucky_number(n):
    other = False
    cnt = 0
    if n == 0:
        return False, cnt
    while n > 0:
        if n % 10 not in [7,4]:
            other = True
        else:
            cnt += 1
        n //= 10
    if not other:
        return True, cnt
    return False, cnt
ans, cnt = lucky_number(n)
ans, cnt = lucky_number(cnt)    
if ans == True:
    print("YES")
else:
    print("NO")