class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        j = 1
        l = len(nums)
        while i<l:
            val = nums[i]
            occur = 1
            # print(i, j, occur)
            while j<l:
                if nums[j] == nums[i]:
                    if occur==2:
                        nums.pop(j)
                        # print(occur, i, j, nums)
                        l -=1
                    else:
                        occur += 1
                        j += 1
                else:
                    break
            i = j
            j = j+1
        # print(nums)
        return len(nums)
