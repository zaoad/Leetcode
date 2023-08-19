class Solution:
    def canJump(self, nums: List[int]) -> bool:
        l = len(nums)
        reachable = 0
        for i , v in enumerate(nums):
            if i > reachable:
                return False
            reachable = max(reachable, i+v)
        return True
