class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {1:1, 2:2}
        def f(i):
            if i in memo:
                return memo[i]
            memo[i] = f(i-1) + f(i-2)
            return memo[i]

        return f(n) 
            
            