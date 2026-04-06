class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        prefix, suffix = [1] * n, [1] * n

        for i, num in enumerate(nums):
            if i == 0:
                continue
            prefix[i] = prefix[i-1] * nums[i-1]

        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i+1]

        for i in range(n):
            result[i] = prefix[i] * suffix[i]

        return result