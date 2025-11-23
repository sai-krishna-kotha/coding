# pattern : prefixSum + hash map
# key idea: prefixSum[j-1] - prefixSum[i] % k == 0 to prefixSum[j-1] % k == prefixSum[i] % k


from typing import List
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        prefix = 0
        hash_map = {0:-1}
        for i, num in enumerate(nums):
            prefix += nums[i]
            prefix_mod_k = prefix % k
            if prefix_mod_k in hash_map:
                if i - hash_map[prefix_mod_k] >= 2:
                    return True
            else:
                hash_map[prefix_mod_k] = i
        return False
