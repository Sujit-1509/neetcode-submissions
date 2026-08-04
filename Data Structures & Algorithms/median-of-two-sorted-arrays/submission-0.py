from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        nums.sort()
        n = len(nums)
        m = n // 2
        
        if n % 2 != 0:  # odd length
            return float(nums[m])
        else:  # even length
            return (nums[m - 1] + nums[m]) / 2.0
