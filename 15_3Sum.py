class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        i = 0
        l = len(nums)
        s = list()
        print(nums)
        while i<l-2:
            if i>0 and nums[i]==nums[i-1]:
                i +=1
                continue
            j=i+1
            k=l-1
            while j<k:
                if j>i+1 and nums[j]==nums[j-1]:
                    j+=1
                    continue
                sum = nums[i]+ nums[j]+nums[k]
                if sum == 0:
                    s.append([nums[i], nums[j], nums[k]])
                    j+=1
                    # print(s)
                elif sum<0:
                    j +=1
                else:
                    k -=1
            i +=1
        return s
