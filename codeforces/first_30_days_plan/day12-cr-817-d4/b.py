# import sys
# sys.setrecursionlimit(1_000_000)

def solve():
    # input = sys.stdin.readline
    t = int(input())
    for _ in range(t):
        cols = int(input())
        row1 = input().strip()
        row2 = input().strip()
        ans = "YES"
        for x, y in zip(row1, row2):
            if x == 'R' and y != 'R' or x != 'R' and y == 'R':
                ans = 'NO'
                break
        print(ans)
    


if __name__ == "__main__":
    solve()