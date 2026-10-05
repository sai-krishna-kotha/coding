import sys
sys.setrecursionlimit(1_000_000)

def solve():
    # input = sys.stdin.readline

    t = int(input())
    # for _ in range(t):
    #     n = int(input())
    #     strings = []
    #     for _ in range(n):
    #         strings.append(input().strip())
    #     ans = [0]*n
    #     for i in range(n):
    #         for j in range(n):
    #             if j == i:
    #                 continue
    #             for k in range(n):
    #                 if k == i:
    #                     continue
    #                 if strings[i] == strings[j] + strings[k]:
    #                     ans[i] = 1
    #     print(''.join(map(str, ans)))


    for _ in range(t):
        n = int(input())

        words = [input().strip() for _ in range(n)]
        word_set = set(words)

        ans = []

        for s in words:
            found = False

            for j in range(1, len(s)):
                left = s[:j]
                right = s[j:]

                if left in word_set and right in word_set:
                    found = True
                    break

            ans.append('1' if found else '0')

        print(''.join(ans))

if __name__ == "__main__":
    solve()