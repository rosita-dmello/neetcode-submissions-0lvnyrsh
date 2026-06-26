class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(string, c, o):
            if o == n and c==n:
                res.append(string)
                return 
            if o < n:
                backtrack(string + '(', c, o+1)
            if c < o:
                backtrack(string + ')', c+1, o)
        
        backtrack('', 0, 0)
        return res