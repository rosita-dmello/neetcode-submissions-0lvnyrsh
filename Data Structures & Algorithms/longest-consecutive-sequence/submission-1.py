class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        starts = set() 
        nums_set = set(nums)
        for num in nums:
            if num-1 not in nums_set:
                starts.add(num)
        lengths = {}
        max_len = 0
        for start in starts:
            lengths[start] = 1
            next_ = start #2
            while next_+1 in nums_set:
                lengths[start] += 1
                next_ += 1
            if lengths[start] > max_len:
                max_len = lengths[start]
    

        return max_len

        