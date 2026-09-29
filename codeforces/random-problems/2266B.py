def solve(a, b, c):
    if a >= b:
        return a - b + c
    return max(b-a, a+c-b)

if __name__ == "__main__":
    n = int(input())
    for _ in range(n):
        a, b, c = (map(int, input().split()))
        ans = solve(a, b, c)
        print(ans)