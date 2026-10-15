# import sys
# sys.setrecursionlimit(1_000_000)

def solve():
    # input = sys.stdin.readline
    t = int(input())
    for _ in range(t):
        num = int(input())
        ans = []
        min_summands = 0
        for i in range(len(str(num))):
            ld = num % 10
            num //= 10
            if ld != 0:
                ans.append(ld * (10**i))
                min_summands += 1
        print(min_summands)
        print(" ".join(map(str, ans)))
            
    


if __name__ == "__main__":
    solve()