import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
    
        min_rate = max(piles)
        
        l = 1
        r = max(piles)

        while l <= r:
            mid = l + ((r-l)//2)
            rate = mid
            hrs = 0
            for pile in piles:
                hrs += math.ceil(pile/rate)
            if hrs <= h:
                min_rate = rate
                r = mid - 1
            else:
                l = mid + 1

        return min_rate 
