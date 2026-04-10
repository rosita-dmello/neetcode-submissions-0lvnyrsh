class Solution:
    def trap(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        res_area = 0
        left_max = height[i]
        right_max = height[j]

        while i < j:
            if left_max <= right_max:
                i = i+1
                if height[i] > left_max:
                    left_max = height[i]
                area = left_max - height[i]
                if area > 0:
                    res_area += area
                
            else:
                j-=1
                if height[j] > right_max:
                    right_max = height[j]
                area = right_max - height[j]
                if area > 0:
                    res_area += area
                
                    
        return res_area


