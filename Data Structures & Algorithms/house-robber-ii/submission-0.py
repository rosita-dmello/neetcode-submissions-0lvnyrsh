class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))

    def helper(self, nums):
        prev, curr = 0, 0

        for num in nums:
            prev, curr = curr, max(prev+num, curr)
        
        return curr

