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
                area = left_max - height[i]
                if area > 0:
                    res_area += area
                if height[i] > left_max:
                    left_max = height[i]
            else:
                j-=1
                area = right_max - height[j]
                if area > 0:
                    res_area += area
                if height[j] > right_max:
                    right_max = height[j]
                    
        return res_area


