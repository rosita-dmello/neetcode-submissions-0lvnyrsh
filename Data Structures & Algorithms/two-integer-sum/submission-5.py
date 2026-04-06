class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices_map = {}
        for i in range(len(nums)):
            indices_map[nums[i]] = i
        for i in range(len(nums)):
            j = nums[i]
            rem = target - j
            if rem in indices_map and indices_map[rem] != i:
                return [i, indices_map[rem]]