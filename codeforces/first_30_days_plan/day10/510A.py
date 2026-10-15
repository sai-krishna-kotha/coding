import sys
sys.setrecursionlimit(1_000_000)

def solve():
    # input = sys.stdin.readline

    m, n = map(int, input().split())
    ans = []
    flag = True
    for i in range(m):
        if i % 2 == 0:
            ans.append('#'*n)
        elif flag:
            ans.append(('.'* (n-1)) + '#')
            flag = not flag
        else:
            ans.append('#' + ('.'* (n-1)))
            flag = not flag
    print('\n'.join(ans))
if __name__ == "__main__":
    solve()