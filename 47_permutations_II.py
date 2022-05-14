from typing import List
from collections import Counter

class Solution:
    def __init__(self):
        self.length = None
        self.list = []
        self.dict_nums = dict()


    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.length = len(nums)
        vis = [0]*self.length
        pset = [-1000]*self.length
        for num in nums:
            if num not in self.dict_nums:
                self.dict_nums[num] = 1
            else:
                self.dict_nums[num] += 1
        t_dict = self.dict_nums.copy()
        self.permutation(nums, t_dict, pset[:], 0)
        print(self.list)
        return self.list


    def permutation(self, nums, t_dict, pset, total):
        if total == self.length:
            self.list.append(pset)
        for i in t_dict:
            if t_dict[i] > 0:
                t_dict[i]-=1
                pset[total] = i
                self.permutation(nums, t_dict.copy(), pset[:], total+1)
                t_dict[i]+=1


s = Solution()
ans = s.permuteUnique([1,2,2,3])
print('ans', ans)

