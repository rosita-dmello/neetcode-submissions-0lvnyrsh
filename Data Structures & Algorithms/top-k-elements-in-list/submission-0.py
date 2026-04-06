class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for i in nums:
            counts[i] = counts.get(i, 0) + 1
        
        sorted_dict = dict(sorted(counts.items(), key = lambda x: x[1], reverse=True))
        return list(sorted_dict.keys())[:k]
        