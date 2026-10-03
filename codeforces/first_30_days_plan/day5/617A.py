import sys
sys.setrecursionlimit(1_000_000)

def solve():
    # input = sys.stdin.readline

    n = int(input())
    ans = n // 5 + (1 if n % 5 != 0 else 0)

    print(ans)
    
if __name__ == "__main__":
    solve()