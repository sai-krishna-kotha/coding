from typing import List
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        right = sum(nums)
        left = 0
        flag = True
        for i in range(len(nums)):
            right -= nums[i]
            if left == right:
                flag = False
                return i
            left += nums[i]
        if flag:
            return -1