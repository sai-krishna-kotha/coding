process = input()
if process == 'first':
    n = int(input())
    arr = list(map(int, input().split()))
    ans1 = []
    for i in range(n):
        ans1.append(chr(96+arr[i]))
    print(''.join(ans1))
else:
    s = list(input())
    ans2 = []
    for i in range(len(s)):
        ans2.append(ord(s[i])-96)
    print(len(s))
    print(' '.join(map(str, ans2)))