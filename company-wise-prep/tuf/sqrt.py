def bs(x):
    low = 0
    high = x//2 + 1
    ans = -1
    while low <= high:
        mid = (low+high)//2
        if mid * mid <= x:
            ans = mid
            low = mid + 1
        elif mid * mid > x:
            high = mid - 1
    return ans
# ans = bs(24)
# print(ans)

def helper1(x, n):
    # ans = 1
    # for i in range(n):
    #     ans *= x
    # return ans
    ans = 1
    while n > 0:
        if n % 2 == 1:
            ans = ans * x
            n = n - 1
        else:
            x = x * x
            n = n // 2
    return ans
def nth_root_m(n, m):
    low = 0
    high = m
    while low <= high:
        mid = (low+high)//2
        x = helper1(mid, n)
        if x == m:
            return mid
        elif x < m:
            low = mid + 1
        else:
            high = mid - 1
    return -1
ans = nth_root_m(4, 1296)
print(ans)
