class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        nums.sort()
        l = len(nums)
        majority_size = int(l/3)
        ans = set()
        for i,v in enumerate(nums):
            if(i== l-majority_size):
                break; 
            val = v
            if(nums[i+majority_size]==v):
                print("v")
                ans.add(v) 
        return list(ans)
