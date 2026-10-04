import sys
sys.setrecursionlimit(1_000_000)

def solve():
    input = sys.stdin.readline

    t = int(input())
    for _ in range(t):
        n = int(input())
        strings = []
        for _ in range(n):
            strings.append(input().strip())
        ans = [0]*n
        for i in range(n):
            for j in range(n):
                if j == i:
                    continue
                for k in range(n):
                    if k == i:
                        continue
                    if strings[i] == strings[j] + strings[k]:
                        ans[i] = 1
        print(''.join(map(str, ans)))

if __name__ == "__main__":
    solve()