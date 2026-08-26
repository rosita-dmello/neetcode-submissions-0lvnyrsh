class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        pre, suff = 1,1
        n = len(nums)
        max_p = nums[0]

        for i in range(n):
            
            pre = nums[i] * pre
            suff = nums[n-i-1] * suff
            max_p = max(max_p, pre, suff)

            if nums[i] == 0:
                pre = 1
            if nums[n-i-1] == 0:
                suff = 1
        return max_p
