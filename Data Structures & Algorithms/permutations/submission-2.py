class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(idx, nums):
            if idx == len(nums):
                res.append(nums[:])
                return
            
            for i in range(idx, len(nums)):
                nums[i], nums[idx] = nums[idx], nums[i]
                backtrack(idx+1, nums)
                nums[idx], nums[i] = nums[i], nums[idx]
        backtrack(0, nums)
        return res 
        