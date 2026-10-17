# import sys
# sys.setrecursionlimit(1_000_000)
from collections import defaultdict
def helper(string):
    ans = 0
    for ch in string:
        ans += ord(ch)
    return ans

def solve():
    # input = sys.stdin.readline
    n, m = map(int, input().split())
    S = set()
    # hashmap = defaultdict(list)
    S = [input().strip() for _ in range(n)]
    S_set = set(S)
    # for _ in range(n):
    #     word = input().strip()
    #     S.add(word)
    #     hashmap[helper(word)].append(word)
    T = [input().strip() for _ in range(m)]
    # print(S)
    # print(hashmap)
    # print(T)
    ans = defaultdict(int)
    for ballet in T:
        if ballet in S_set:
            ans[ballet] += 1
            continue
        word = -1
        for target in S_set:
            if len(ballet) == len(target):
                miss = sum(1 for c1, c2 in zip(ballet, target) if c1 != c2)
                if miss == 1:
                    if word == -1:
                        word = target
                    else:
                        word = 0
        if word != -1 and word != 0:
            ans[word] += 1
            
    for cand in S:
        print(ans[cand])
        
    


if __name__ == "__main__":
    solve()