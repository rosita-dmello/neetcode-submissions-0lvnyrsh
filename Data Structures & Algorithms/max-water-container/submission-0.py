class Solution:
    def maxArea(self, nums: List[int]) -> int:
        i = 0 
        j = len(nums) - 1
        max_ar = -1
        
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                length = j - i
                breadth = min(nums[i], nums[j])
                area = length*breadth
                if area > max_ar:
                    max_ar = area       
            
        return max_ar