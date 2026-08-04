class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = 0
        max_count = 0
        arr = []

        for i in s:
            val = ord(i) - ord("a")
            if val in arr:
                # remove everything up to the duplicate
                dup_index = arr.index(val)
                arr = arr[dup_index+1:]
            arr.append(val)
            count = len(arr)
            max_count = max(max_count, count)

        return max_count
