from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = -100005
        finalMax = -100005
        for num in nums:
            maxSum = max(num, maxSum + num)
            finalMax = max(maxSum, finalMax)
        return finalMax

