class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def backtrack(i, subs):
            if i == len(nums):
                res.append(subs[:])
                return
            subs.append(nums[i])
            backtrack(i+1, subs)
            subs.pop()
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i+=1
            backtrack(i+1, subs)
        backtrack(0, [])

        return res