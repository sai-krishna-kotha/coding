import sys
sys.setrecursionlimit(1_000_000)
# input = sys.stdin.readline

def solution(n):
    while n <= 9999:
        n += 1
        if len(set(str(n))) == 4:
            return n





if __name__ == "__main__":
    # take input
    n = int(input().strip())
    ans = solution(n)
    print(ans)