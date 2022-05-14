from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        t=None
        ans = 0
        for n in nums:
            if t != n:
                nums[ans] = n
                ans += 1
                t = n
            # print(nums)
        return ans