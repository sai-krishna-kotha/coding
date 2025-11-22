# pattern: prefix, suffix products , array
# key idea: precalculate prefix and suffix prods

from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = [1]*n
        right = [1]*n
        prefix = 1
        suffix = 1
        for i in range(1, n):
            prefix = prefix * nums[i-1]
            left[i] = prefix
            i = n - i - 1
            suffix = suffix * nums[i+1]
            right[i] = suffix
        ans = []
        for i in range(n):
            ans.append(left[i]*right[i])
        return ans