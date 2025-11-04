nums = list(map(int, input()))
for i in range(len(nums)):
    if i == 0 and nums[i] != 9 and nums[i] > 4:
        nums[i] = 9 - nums[i]
    elif i != 0 and nums[i] > 4:
        nums[i] = 9 - nums[i]
nums = list(map(str, nums))
print(''.join(nums))