class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        nums = list(set(nums))
        diff = []
        if len(nums) == 0:
            return 0
        else:
            for i in range(len(nums) - 1):
                diff.append(nums[i + 1] - nums[i])
        return diff.count(1) + 1
  

        