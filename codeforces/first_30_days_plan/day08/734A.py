import sys
sys.setrecursionlimit(1_000_000)

def solve():
    # input = sys.stdin.readline

    n = int(input())
    s = input().strip()
    a_count = s.count('A')
    d_count = len(s) - a_count
    if a_count > d_count:
        ans = 'Anton'
    elif a_count < d_count:
        ans = 'Danik'
    else:
        ans = 'Friendship'
    print(ans)

if __name__ == "__main__":
    solve()