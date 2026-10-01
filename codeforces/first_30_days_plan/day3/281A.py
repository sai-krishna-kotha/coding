import sys
sys.setrecursionlimit(1_000_000)

def solve():
    input = sys.stdin.readline

    word = input()
    if word[0].istitle():
        ans = word
    else:
        ans = word[0].upper() + (word[1:] if len(word) > 1 else '')
    print(ans)
if __name__ == "__main__":
    solve()