class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        max_prof = 0

        while r < len(prices):
            if prices[r] > prices[l]:
                max_prof = max(max_prof, prices[r] - prices[l])
                r = r + 1
            else:
                l = r
                r = r + 1
        return max_prof
