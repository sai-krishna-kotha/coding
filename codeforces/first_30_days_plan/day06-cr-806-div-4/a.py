import sys
sys.setrecursionlimit(1_000_000)

def solve():
    # input = sys.stdin.readline

    t = int(input())
    for _ in range(t):
        s = input().lower()
        if s == 'yes':
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    solve()