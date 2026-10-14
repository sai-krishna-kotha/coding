import sys
sys.setrecursionlimit(1_000_000)

def solve():
    input = sys.stdin.readline

    n, h = map(int, input().split())
    arr = list(map(int, input().split()))
    ans = 0
    for ele in arr:
        if ele > h:
            ans += 2
        else:
            ans += 1
    print(ans)

if __name__ == "__main__":
    solve()