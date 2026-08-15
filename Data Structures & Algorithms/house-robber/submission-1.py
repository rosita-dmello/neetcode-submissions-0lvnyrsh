class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        memo = [-1] * n
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        memo[0] = nums[0]
        memo[1] = max(nums[0], nums[1])

        def f(i):
            if memo[i] != -1:
                return memo[i]
            memo[i] = max(f(i-1), f(i-2) + nums[i])
            return memo[i]
        return f(n-1)