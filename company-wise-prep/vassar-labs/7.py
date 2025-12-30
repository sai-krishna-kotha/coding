def dutch_national_flag(nums: list):
    def swap(nums, a, b):
            nums[a], nums[b] = nums[b], nums[a]
    start = 0
    end = len(nums)-1
    mid = 0
    while mid <= end:
        if nums[mid] == 0:
            swap(nums, start, mid)
            start += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            swap(nums, mid, end)
            end -= 1
    return

arr = [2,0,2,1,1,0]
dutch_national_flag(arr)
print(arr)