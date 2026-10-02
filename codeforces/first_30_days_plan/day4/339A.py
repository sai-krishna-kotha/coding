import sys
sys.setrecursionlimit(1_000_000)

def solve():
    # input = sys.stdin.readline

    summonds = list(map(int, input().split('+')))
    summonds.sort()
    print('+'.join(map(str, summonds)))

if __name__ == "__main__":
    solve()