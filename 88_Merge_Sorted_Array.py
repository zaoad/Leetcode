class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums3 = []
        i = 0;
        j = 0;
        while i<m or j<n:
            if i>=m:
                nums3.append(nums2[j])
                j += 1
                continue
            if j>=n:
                nums3.append(nums1[i])
                i += 1
                continue
            if nums1[i] < nums2[j]:
                nums3.append(nums1[i])
                i +=1
            else:
                nums3.append(nums2[j])
                j +=1
        for k, v in enumerate(nums3):
            nums1[k] = v
