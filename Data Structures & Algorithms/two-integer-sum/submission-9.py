class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices_map = {}      
        for i, n in enumerate(nums):
            rem = target - n
            if rem in indices_map and indices_map[rem] != i:
                return [indices_map[rem], i]
            else:
                indices_map[n] = i