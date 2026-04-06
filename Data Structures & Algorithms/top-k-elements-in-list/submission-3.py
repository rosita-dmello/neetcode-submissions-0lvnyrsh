class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for i in range(len(nums)+1)] 
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        for n, c in count.items():
            freq[c].append(n)
    
        result = []
        for i in range(len(freq)-1, 0, -1):
            for j in freq[i]:
                if len(result) < k:
                    result.append(j)
                else:
                    break
            if len(result) == k:
                break
        return result

            
        