from typing import List


class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        dict={}
        for num in nums:
            if num not in dict:
                dict[num]=1
            else:
                dict[num]=dict[num]+1
        count=0
        sum=0
        for index in dict:
            if dict[index]==1:
                sum=sum+index
        return sum