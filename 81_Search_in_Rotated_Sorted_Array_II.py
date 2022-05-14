from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        p = self.find_pivot(nums)
        # print('pivot', p)
        low = p
        s = len(nums)
        high = p + s
        while low <= high:
            mid = int((low + high) / 2)
            check=mid%s
            # print(low, high, mid, check)
            if nums[check] == target:
                return True
            if target < nums[check]:
                high =  mid-1
            else:
                low = mid+1
            # print(low, high)
        return False

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
            # print(left, right, mid)
            if nums[mid] > nums[(mid + 1)]:
                return mid + 1
            if nums[mid] >= nums[left]:
                left = left + 1
            else:
                right = right - 1
        return left
