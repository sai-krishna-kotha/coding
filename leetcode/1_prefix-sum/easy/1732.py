from typing import List
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        first = 0
        ans = 0
        for i in range(len(gain)):
            first = gain[i] + first 
            ans = max(ans, first)
        return ans