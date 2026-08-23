class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]

        cur_min, cur_max = 1,1

        for n in nums:
            tmp = cur_min
            cur_min = min(cur_min * n, cur_max * n, n)
            cur_max = max(tmp * n, cur_max * n, n)
            res = max(res, cur_max)    

        return res
        

