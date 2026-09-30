import sys
sys.setrecursionlimit(1_000_000)

def solve():
    input = sys.stdin.readline

    t = 5
    x = y = 0
    flag = False
    for i in range(t):
        arr = list(map(int, input().split()))
        if sum(arr) == 1:
            for k in range(t):
                if arr[k] == 1:
                    x = i
                    y = k
                    flag = True
                    break
        if flag:
            break
    print(abs(2-x) + abs(2-y))
        

        # write logic here
        # ans = ...
        # print(ans)

if __name__ == "__main__":
    solve()