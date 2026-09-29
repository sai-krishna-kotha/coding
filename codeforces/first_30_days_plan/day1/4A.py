import sys
input = sys.stdin.readline

def solution(n):
    return "YES" if n % 2 == 0 and n > 2 else "NO"




if __name__ == "__main__":
    n = int(input())
    ans = solution(n)
    print(ans)