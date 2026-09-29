import sys
sys.setrecursionlimit(1_000_000)

def solve():
    input = sys.stdin.readline

    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))

        # write logic here
        # ans = ...
        # print(ans)

if __name__ == "__main__":
    solve()