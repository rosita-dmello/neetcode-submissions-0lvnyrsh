class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_buy = prices[0]
        max_prof = 0

        for sell in prices:
            prof = sell - min_buy
            max_prof = max(prof, max_prof)
            min_buy = min(sell, min_buy)
    
        return max_prof