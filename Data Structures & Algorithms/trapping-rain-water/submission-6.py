class Solution:
    def trap(self, height: List[int]) -> int:
        soln = 0
        
        i = 0
        j = len(height) - 1
        l_max = 0
        r_max = 0


        while i <= j:
            if l_max <= r_max:
                l_max = max(l_max, height[i])
                area = l_max - height[i]
                if area > 0:
                    soln += area
                i+=1
                
            else:
                r_max = max(r_max, height[j])
                area = r_max - height[j]
                if area > 0:
                    soln += area
                j-=1
                

        return soln