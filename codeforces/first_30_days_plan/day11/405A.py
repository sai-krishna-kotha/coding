# import sys
# sys.setrecursionlimit(1_000_000)

def solve():
    # input = sys.stdin.readline
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    print(' '.join(map(str, arr)))
    


if __name__ == "__main__":
    solve()