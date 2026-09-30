import sys
sys.setrecursionlimit(1_000_000)

def solve():
    input = sys.stdin.readline

    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    target = arr[k-1]
    ans = 0
    for i in range(n):
        if arr[i] <= 0:
            break
        elif arr[i] >= target:
            ans += 1
    print(ans)
if __name__ == "__main__":
    solve()