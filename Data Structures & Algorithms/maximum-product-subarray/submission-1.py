class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]

        curr_min, curr_max = 1, 1

        for num in nums:
            temp = curr_min
            curr_min = min(curr_min * num, curr_max * num, num)
            curr_max = max(curr_max * num, temp * num, num)
            res = max(curr_max, res)
        
        return res