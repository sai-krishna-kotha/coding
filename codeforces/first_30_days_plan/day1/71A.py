import sys
sys.setrecursionlimit(1_000_000)
# input = sys.stdin.readline

def solution(word):
    if len(word) > 10:
        return f"{word[0]}{len(word)-2}{word[-1]}" 
    return word




if __name__ == "__main__":
    # take input
    for _ in range(int(input())):
        word = input()
        ans = solution(word)
        print(ans)