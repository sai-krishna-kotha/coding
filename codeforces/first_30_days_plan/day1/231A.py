import sys
sys.setrecursionlimit(1_000_000)

def solution():
    # input = sys.stdin.readline
    ans = 0
    for _ in range(int(input())):
        question = list(map(int, input().split()))
        if sum(question) >= 2:
            ans += 1
    print(ans)



if __name__ == "__main__":
    solution()
