import sys
sys.setrecursionlimit(1_000_000)

def solve():
    # input = sys.stdin.readline
    inp_year = int(input())
    temp = inp_year + 1
    while temp <= 9999:
        if len(set(str(temp))) == 4:
            print(temp)
            break
        temp += 1
    

if __name__ == "__main__":
    solve()