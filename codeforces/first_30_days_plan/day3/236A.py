import sys
sys.setrecursionlimit(1_000_000)

def solve():
    # input = sys.stdin.readline

    user_name = input()
    # ans = ''
    # if len(set(user_name)) % 2 == 0:
    #     ans = 'CHAT WITH HER!'
    # else:
    #     ans = 'IGNORE HIM!'
    # print(ans)
    
    ans = ''
    freq = [0]* 26
    for ch in user_name:
        freq[ord(ch) - ord('a')] += 1
    unique_chars = 0
    for cnt in freq:
        if cnt > 0:
            unique_chars += 1
    if unique_chars % 2 == 0:
        ans = 'CHAT WITH HER!'
    else:
        ans = 'IGNORE HIM!'
    print(ans)
if __name__ == "__main__":
    solve()