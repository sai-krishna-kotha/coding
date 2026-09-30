import sys
sys.setrecursionlimit(1_000_000)

def solve():
    # input = sys.stdin.readline

    t = int(input())
    ans = 0
    for _ in range(t):
        operation = input()
        if operation == '++X' or operation == 'X++':
            ans += 1
        else:
            ans -= 1
    print(ans)

        

if __name__ == "__main__":
    solve()