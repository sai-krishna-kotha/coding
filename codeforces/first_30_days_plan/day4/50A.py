import sys
sys.setrecursionlimit(1_000_000)

def solve():
    input = sys.stdin.readline

    rows, cols = map(int, input().split())
    
    ans = (rows // 2) * cols
    if rows % 2 == 1:
        ans += cols // 2
    
    print(ans)

if __name__ == "__main__":
    solve()