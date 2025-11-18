from typing import List
class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        left = 0
        right = sum(nums)
        ans = [0]*len(nums)
        for i in range(len(nums)):
            right -= nums[i]
            ans[i] = abs(left-right)
            left += nums[i]
        return ans