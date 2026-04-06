class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for n in nums:
            count[n] += 1
        freq_buckets = [[] for i in range(len(nums))]

        for num, cnt in count.items():
            freq_buckets[cnt-1].append(num)
        res = []
        for i in range(len(freq_buckets)-1, -1, -1):
            for n in freq_buckets[i]:
                if len(res) < k:
                    res.append(n)
        return res
