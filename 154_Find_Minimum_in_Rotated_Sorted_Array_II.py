from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        p = self.find_pivot(nums)
        return nums[p]

    def find_pivot(self, nums) -> int:
        if len(nums) == 1:
            return 0
        left = 0
        right = len(nums) - 1
        s = len(nums)
        if (nums[left] < nums[right]):
            return 0;
        while left < right:
            mid = int((left + right) / 2)
            print(left, right, mid)
            if nums[mid] > nums[(mid + 1)]:
                return mid + 1
            if nums[mid] == nums[right]:
                right -=1
            elif nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid - 1
        return left