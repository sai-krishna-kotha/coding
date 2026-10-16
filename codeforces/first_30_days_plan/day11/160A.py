# import sys
# sys.setrecursionlimit(1_000_000)

def solve():
    # input = sys.stdin.readline
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)
    total_sum = sum(arr)
    temp = 0
    ans = 0
    for ele in arr:
        if temp <= total_sum - temp:
            temp += ele
            ans += 1
        else:
            break
    print(ans)

if __name__ == "__main__":
    solve()