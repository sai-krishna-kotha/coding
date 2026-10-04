import sys
sys.setrecursionlimit(1_000_000)

def solve():
    # input = sys.stdin.readline

    t = int(input())
    for _ in range(t):
        n = int(input())
        s = list(input())
        freq = [0]* 26
        for ch in s:
            freq[ord(ch) - ord('A')] += 1
        ans = 0
        for cnt in freq:
            if cnt > 0:
                ans += (cnt + 1)
        print(ans)

if __name__ == "__main__":
    solve()