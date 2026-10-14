import sys
sys.setrecursionlimit(1_000_000)

def solve():
    # input = sys.stdin.readline

    inn = input().strip()
    if len(inn) == 2: 
        print(0)
    else:
        sett = set(inn.strip()[1:-1].split(', '))
        print(len(sett))
if __name__ == "__main__":
    solve()