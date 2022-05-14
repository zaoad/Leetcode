from typing import List


class Solution:
    def __init__(self):
        self.length = None
        self.list = []


    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.length = len(nums)
        vis = [0]*self.length
        pset = [-1000]*self.length
        self.permutation(nums, pset[:], 0, vis[:])
        print(self.list)
        return self.list


    def permutation(self, nums, pset, total, vis):
        if total == self.length:
            self.list.append(pset)
        for i in range(len(vis)):
            if vis[i] == 0:
                vis[i] = 1
                pset[total] = nums[i]
                self.permutation(nums, pset[:], total+1, vis[:])
                vis[i] = 0

s = Solution()
ans = s.permuteUnique([1,2,3])
print('ans', ans)