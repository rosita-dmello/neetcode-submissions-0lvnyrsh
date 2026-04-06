class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        starts = set() 
        nums_set = set(nums)
        max_len = 0
        for num in nums:
            if num-1 not in nums_set:
                length = 1
                next_ = num
                while next_+1 in nums_set:
                    length += 1
                    next_ += 1
                if length > max_len:
                    max_len = length
        return max_len

        