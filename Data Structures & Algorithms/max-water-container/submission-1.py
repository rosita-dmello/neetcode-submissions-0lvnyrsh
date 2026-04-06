class Solution:
    def maxArea(self, nums: List[int]) -> int:
        i = 0 
        j = len(nums) - 1
        max_ar = -1
        
        while i < j:
            length = j - i
            breadth = min(nums[i], nums[j])
            area = length*breadth
            if area > max_ar:
                max_ar = area
            if nums[i] < nums[j]:
                i+=1
            else:
                j-=1
            
        return max_ar