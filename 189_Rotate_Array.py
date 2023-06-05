class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        start = 0
        count = 0
        next = 0
        prev = 0
        it = 0
        l =  len(nums)
        
        while count<l:
             
            next = (start+k)%l
            nums[start], nums[next] = nums[next], nums[start]
            count +=1
            # print(1, nums)
            while next!=start:
                next = (next+k)%l
                # print(start, next)
                nums[start], nums[next] = nums[next], nums[start]
                count +=1
                # print(2,nums)
            start = next+1
        # print(nums)
            
