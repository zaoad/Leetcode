class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # boyes more solution:
        val = nums[0]
        count = 0
        for v in nums:
            if count==0:
                val = v
                count+=1
            elif v==val:
                count+=1
            else:
                count -=1
        return val    
                
