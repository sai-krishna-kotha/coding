import sys
sys.setrecursionlimit(1_000_000)

def solve():
    input = sys.stdin.readline

    y, w = map(int, input().split())
    chances = 6 - max(y, w) + 1
    ans = ''
    if chances == 6:
        ans = '1/1'
    elif chances == 5:
        ans = '5/6'
    elif chances == 4:
        ans = '2/3'
    elif chances == 3:
        ans = '1/2'
    elif chances == 2:
        ans = '1/3'
    elif chances == 1:
        ans = '1/6'
    else:
        ans = '0/1'
        
    print(ans)
if __name__ == "__main__":
    solve()