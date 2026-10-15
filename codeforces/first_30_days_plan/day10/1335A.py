# import sys
# sys.setrecursionlimit(1_000_000)

def solve():
    # input = sys.stdin.readline
    t = int(input())
    for _ in range(t):
        num = int(input())
        if num % 2 == 1:
            num -= 1
        else:
            num -= 2
        print(num//2)
    


if __name__ == "__main__":
    solve()