import sys
sys.setrecursionlimit(1_000_000)

def solve():
    input = sys.stdin.readline

    t = int(input())
    for _ in range(t):
        n = int(input())
        starting_digits = list(map(int, input().split()))
        ans = [0]*n
        for i in range(n):
            x, moves = map(str, input().split())
            d_moves = moves.count('D')
            ans[i] = (starting_digits[i] + d_moves - (int(x) - d_moves)) % 10
        print(' '.join(map(str, ans))) 
            # print(int(x), moves)
        # write logic here
        # ans = ...
        # print(ans)

if __name__ == "__main__":
    solve()