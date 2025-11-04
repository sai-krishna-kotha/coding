n = int(input())
for _ in range(n):
    a1, a2, a4, a5 = map(int, input().split())
    ans1 = a1 + a2
    ans2 = a4 - a2
    ans3 = a5 - a4
    if ans1 == ans2 and ans2 == ans3:
        print(3)
    elif ans1 == ans2 or ans1 == ans3 or ans2 == ans3:
        print(2)
    else:
        print(1)