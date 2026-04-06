class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n

        prefix_prod = 1
        for i in range(n):
             result[i] = prefix_prod
             prefix_prod = prefix_prod * nums[i]
        
        suffix_prod = 1
        for i in range(n-1, -1, -1):
            result[i] = result[i] * suffix_prod
            suffix_prod = suffix_prod * nums[i]

        return result