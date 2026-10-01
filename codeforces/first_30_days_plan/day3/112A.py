import sys
sys.setrecursionlimit(1_000_000)

def solve():
    # input = sys.stdin.readline

    str_a = input().lower()
    str_b = input().lower()
    ans = 0
    for i in range(len(str_a)):
        if str_a[i] < str_b[i]:
            ans = -1
            break
        elif str_a[i] > str_b[i]:
            ans = 1
            break
    
    print(ans)

if __name__ == "__main__":
    solve()