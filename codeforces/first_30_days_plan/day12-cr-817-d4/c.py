# import sys
# sys.setrecursionlimit(1_000_000)
from collections import defaultdict
def solve():
    # input = sys.stdin.readline
    t = int(input())
    for _ in range(t):
        words = int(input())
        first_person = input().split()
        second_person = input().split()
        third_person = input().split()
        
        dici = defaultdict(list)
        for x, y, z in zip(first_person, second_person, third_person):
            dici[x].append(0)
            dici[y].append(1)
            dici[z].append(2)
        # print(dici)
        ans = [0]*3
        for k, v in dici.items():
            if len(v) == 1:
                ans[v[0]] += 3
            elif len(v) == 2:
                ans[v[0]] += 1
                ans[v[1]] += 1
        print(*ans)
            
            



if __name__ == "__main__":
    solve()