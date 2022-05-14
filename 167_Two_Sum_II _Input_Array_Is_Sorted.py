from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) -1
        while i<j:
            sum = numbers[i]+numbers[j]
            # print(sum,i,j)
            if sum == target:
                # print(sum)
                return [i+1,j+1]
            if sum < target:
                i+=1
            else:
                j-=1


s = Solution()
ans = s.twoSum([2,7,11,15],9)
print(ans)