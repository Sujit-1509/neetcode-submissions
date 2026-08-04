class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        nums = sorted(set(nums))    # Remove duplicates
        diff = []

        for i in range(len(nums) - 1):
            diff.append(nums[i + 1] - nums[i])

        longest = 1
        current = 1

        for d in diff:
            if d == 1:
                current += 1
            else:
                longest = max(longest, current)
                current = 1

        return max(longest, current)