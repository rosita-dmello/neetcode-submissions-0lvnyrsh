class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones_neg = [-i for i in stones]
        heapq.heapify(stones_neg)

        while len(stones_neg) > 1:
            stone1 = -heapq.heappop(stones_neg)
            stone2 = -heapq.heappop(stones_neg)

            if stone1 > stone2:
                heapq.heappush(stones_neg, -(stone1-stone2))
        
        if len(stones_neg) == 1:
            return -stones_neg[0]
        return 0