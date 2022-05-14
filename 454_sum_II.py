from typing import List
from collections import defaultdict

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        dict, ans = defaultdict(int), 0
        for i in nums1:
            for j in nums2:
                dict[i+j] +=1
        for k in nums3:
            for l in nums4:
                ans += dict[0 - (k + l)]
        return ans

s = Solution()
s.fourSumCount()