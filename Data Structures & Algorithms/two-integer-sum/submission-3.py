class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        matrix = []
        occ = {}

        for index, num in enumerate(nums):
            rem = target - nums[index]
            if occ.get(rem, None) is not None:
                return [occ.get(rem), index]
            occ[num] = index
        return []