from collections import Counter
for _ in range(int(input())):
    n = int(input())
    s1, s2 = map(str, input().split())
    freq1 = Counter(s1)
    freq2 = Counter(s2)
    flag = 0
    for ch in s1:
        if freq1[ch] != freq2[ch]:
            print("NO")
            flag = 1
            break
    if flag == 0:
        print('YES')