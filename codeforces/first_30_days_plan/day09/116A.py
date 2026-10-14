import sys
sys.setrecursionlimit(1_000_000)

def solve():
    # input = sys.stdin.readline
    n = int(input())
    temp = 0
    ans = 0
    for _ in range(n):
        out, inn = map(int, input().split())
        temp = temp - out + inn
        ans = max(ans, temp)
    print(ans)
    

if __name__ == "__main__":
    solve()