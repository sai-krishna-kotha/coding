# import sys
# sys.setrecursionlimit(1_000_000)

def solve():
    # input = sys.stdin.readline
    arr = list(map(int, input().strip()))
    n = len(arr)
    left = 0
    ans = "NO"
    for right in range(n):
        if arr[left] != arr[right]:
            left = right
        elif right - left + 1 >= 7:
            ans = "YES"
            break
    print(ans)

if __name__ == "__main__":
    solve()