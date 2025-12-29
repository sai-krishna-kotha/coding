# Facorial of a number
# first approach
# O(n), O(1)
def sol(n: int):
    ans = 1
    for i in range(2, n+1):
        ans *= i
    return ans
print(sol(4))