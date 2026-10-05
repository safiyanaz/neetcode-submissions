class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        import numpy as np
        nums1.extend(nums2)
        return float(np.median(nums1))
