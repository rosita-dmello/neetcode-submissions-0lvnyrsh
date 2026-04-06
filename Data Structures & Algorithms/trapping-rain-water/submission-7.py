class Solution:
    def trap(self, height: List[int]) -> int:
        soln = 0
        
        i = 0
        j = len(height) - 1
        l_max = 0
        r_max = 0


        while i <= j:
            if l_max <= r_max:
                
                area = l_max - height[i]
                if area > 0:
                    soln += area
                l_max = max(l_max, height[i])
                i+=1
                
            else:
                
                area = r_max - height[j]
                if area > 0:
                    soln += area
                r_max = max(r_max, height[j])
                j-=1
                

        return soln