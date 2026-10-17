# import sys
# sys.setrecursionlimit(1_000_000)
from collections import Counter
def solve():
    # input = sys.stdin.readline
    t = int(input())
    timur = Counter("Timur")
    for _ in range(t):
        ans = "YES"
        n = int(input())
        string = input().strip()
        if n != 5:
            ans = "NO"
        if timur != Counter(string):
            ans = "NO"
        print(ans)
    


if __name__ == "__main__":
    solve()