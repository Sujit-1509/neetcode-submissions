from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        res = 0
        for i in range(len(height)):
            rightMAX = leftMAX = height[i]
            for j in range(i):
                leftMAX = max(leftMAX, height[j])
            for k in range(i + 1, len(height)):
                rightMAX = max(rightMAX, height[k])
            res += min(leftMAX,rightMAX) - height[i]
        return res          
   