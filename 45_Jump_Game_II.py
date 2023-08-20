class Solution:
    def jump(self, nums: List[int]) -> int:
        jump=0
        cur = 0;
        max_jump = 0
        l = len(nums)
        for i, v in enumerate(nums):
            max_jump = max(max_jump, i+v)
            if i==l-1:
                return jump
            if i > max_jump:
                return -1
            if i==cur:
                cur = max_jump
                jump +=1
        return jump
