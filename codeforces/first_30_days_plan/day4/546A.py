import sys
sys.setrecursionlimit(1_000_000)

def solve():
    input = sys.stdin.readline

    k, n, w = map(int, input().split())
    dollars_need = 0
    for i in range(1, w + 1):
        dollars_need += i * k
    borrow = dollars_need - n
    ans = 0
    if borrow > 0:
        ans = borrow
    
    print(ans)
    

if __name__ == "__main__":
    solve()