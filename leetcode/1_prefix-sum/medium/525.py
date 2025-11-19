from typing import List
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        dici = {0:-1}
        prefix = 0
        ans = 0
        for i, ele in enumerate(nums):
            if ele == 0:
                prefix -= 1
            else:
                prefix += 1
            if prefix in dici:
                ans = max(ans, i - dici[prefix])
            else:
                dici[prefix] = i
        return ans