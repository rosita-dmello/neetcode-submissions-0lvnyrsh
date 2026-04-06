class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        nr = len(matrix)
        nc = len(matrix[0])
        l = 0
        r = (nc*nr) - 1

        while l <= r:
            mid_i = l + ((r-l)//2)  
            print("mid_i", mid_i)
            mid_n = matrix[mid_i//nc][mid_i%nc]
            print("mid_n", mid_n)
            if mid_n == target:
                return True
            elif mid_n > target:
                r = mid_i - 1
            else:
                l = mid_i + 1
        return False     