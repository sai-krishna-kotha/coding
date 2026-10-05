import sys
sys.setrecursionlimit(1_000_000)

def solve():
    input = sys.stdin.readline

    t = int(input())
    arr = [int(input()) for _ in range(t)]
    ans = 1
    for i in range(t-1):
        if arr[i] != arr[i+1]:
            ans += 1
    
    print(ans)
if __name__ == "__main__":
    solve()