# pattern : prefix sum + hashmap
# key idea : odd_count[l-1] = odd_count[r] - k

from typing import List
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        hashmap = {0:1}
        prefix = 0
        ans = 0
        for i, num in enumerate(nums):
            prefix += (num % 2)
            if prefix - k in hashmap:
                ans += hashmap[prefix-k]
            hashmap[prefix] = hashmap.get(prefix, 0) + 1
        return ans