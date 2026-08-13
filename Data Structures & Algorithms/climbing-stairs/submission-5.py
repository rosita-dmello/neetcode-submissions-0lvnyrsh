class Solution:
    def climbStairs(self, n: int) -> int:
        first, second = 1, 2

        if n <= 2:
            return n
        
        for i in range(2, n):
            first, second = second, first + second

        return second