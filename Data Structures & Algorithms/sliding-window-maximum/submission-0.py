class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        arr = []
        for r in range(0, len(nums) - (k - 1)):
            arr.append(max(nums[r: (r + k)]))
        return arr    