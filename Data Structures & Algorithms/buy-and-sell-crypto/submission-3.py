class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                res = max(res, prices[j] - prices[i])
        if res < 0:
            return 0
        else:
            return res          





        