# import sys
# sys.setrecursionlimit(1_000_000)

def solve():
    # input = sys.stdin.readline
    x = list(input())
    y = list(input())
    ans = "Yes"
    if x[0] == 'A' and y[1] == 'D' or \
        x[0] == 'D' and y[1] == 'A' or \
        x[1] == 'A' and y[0] == 'D' or \
        x[1] == 'D' and y[0] == 'A':
            ans = "No"
    print(ans)


if __name__ == "__main__":
    solve()