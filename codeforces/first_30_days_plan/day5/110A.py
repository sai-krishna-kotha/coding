import sys
sys.setrecursionlimit(1_000_000)

def solve():
    # input = sys.stdin.readline

    n = int(input())
    no_of_lucky_digits = 0
    while n > 0:
        ld = n % 10
        if ld == 4 or ld == 7:
            no_of_lucky_digits += 1
        n //= 10
    ans = "NO"
    if no_of_lucky_digits == 4 or no_of_lucky_digits == 7:
        ans = "YES"
    print(ans)

if __name__ == "__main__":
    solve()