import sys
sys.setrecursionlimit(1_000_000)

def solve():
    # input = sys.stdin.readline

    arr = list(map(int, input().split(  )))
    ans = 4 - len(set(arr))
    
    print(ans)

if __name__ == "__main__":
    solve()