class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        countGroups = [[] for i in range(len(nums) + 1)]
        for i in nums:
            counts[i] = counts.get(i, 0) + 1
        for pair in counts.items():
            countGroups[pair[1]].append(pair[0])
        

        res = []
        for i in range(len(countGroups)- 1, 0, -1):
            for num in countGroups[i]:
                if num is not None:
                    res.append(num)
                if len(res) == k:
                    return res

        
        