from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxProd=1
        finalProd=-100005
        minProd=1
        for num in nums:
            maxP=max(num,maxProd*num,minProd*num)
            minProd=min(num,maxProd*num,minProd*num)
            finalProd=max(finalProd,maxP,minProd)
            maxProd=maxP
            # print(num,maxProd,minProd,finalProd)
        return finalProd