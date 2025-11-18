from typing import List
class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        temp = 0
        ans = float('inf')
        for i in range(len(nums)):
            temp += nums[i]
            ans = min(ans, temp)
        if ans < 1:
            return abs(ans) + 1
        return 1