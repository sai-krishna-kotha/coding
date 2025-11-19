# pattern: prefix sum + hashmap
# idea: prefix[r] - prefix[l-1] = k, prefix[l-1] in map?

from typing import List
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = 0
        map = {0:1}
        ans = 0
        for i, ele in enumerate(nums):
            prefix += ele
            if prefix - k in map:
                ans += map[prefix-k]
            map[prefix] = map.get(prefix, 0) + 1
        return ans