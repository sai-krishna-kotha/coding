n = int(input())
nums = list(map(int, input().split()))
ans = 1
temp = ans
for i in range(1, n):
    if nums[i] > nums[i-1]:
        temp += 1
    else:
        temp = 1
    ans = max(ans, temp)
print(ans)