# pattern: prefix sum 
n = int(input())
arr = list(map(int, input().split()))
prefix_sum = 0
i = 0
while prefix_sum < n:
    prefix_sum += arr[i]
    i = (i + 1) % 7
if i == 0:
    print(7)
else:
    print(i)