import sys
sys.setrecursionlimit(1_000_000)

def solve():
    input = sys.stdin.readline

    t = int(input())
    arr = list(map(int, input().split()))
    mapp = dict()
    for i, ele in enumerate(arr):
        mapp[ele] = i+1
    ans = []
    for i in range(len(arr)):
        ans.append(mapp[i+1])
    
    print(' '.join(map(str, ans)))

if __name__ == "__main__":
    solve()