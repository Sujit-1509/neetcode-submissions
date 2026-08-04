class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_sorted = sorted(s1)
        r = len(s1)
        arr = []
        
        for i in range(len(s2) - r + 1):   # loop through all substrings of length r
            arr.append(sorted(s2[i:i + r]))
        
        return s1_sorted in arr
