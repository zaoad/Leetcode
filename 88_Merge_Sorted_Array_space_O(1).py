class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums3 = []
        i = m-1;
        j = n-1;
        k = m+n -1
        while i>=0 or j>=0:
            if i<0:
                nums1[k] = nums2[j]
                k -=1
                j -=1
                continue
            if j<0:
                nums1[k] = nums1[i]
                k -= 1
                i -= 1
                continue
            if nums2[j] >= nums1[i]:
                nums1[k] = nums2[j];
                k -=1
                j -=1
            else:
                nums1[k] = nums1[i]
                k -= 1
                i -= 1
