from typing import List
class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        posSum=0
        negSum=0
        maxSum=0
        for num in nums:
            posSum=max(num,posSum+num)
            negSum=min(num,negSum+num)
            maxSum=max(maxSum,posSum,abs(negSum))
        return maxSum