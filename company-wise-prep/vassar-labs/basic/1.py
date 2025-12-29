# Sum of all odd prime number from 1 to n
# first approach
# O(n**2), O(1)
def sol(n: int):
    ans = 0
    for i in range(3, n+1):
        prime = True
        for j in range(2, int(i**0.5)+1):
            if i % j == 0:
                prime = False
                break
        if prime:
            ans += i
    return ans

ans = sol(25)
print(ans)