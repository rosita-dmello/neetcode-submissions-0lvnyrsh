class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []

        for c in points:
            x, y = c[0], c[1]
            distance = math.sqrt(x*x + y*y)
            heapq.heappush(res, (-distance, c))
            while len(res) > k:
                heapq.heappop(res)
        
        result = [p[1] for p in res]
        return result
            