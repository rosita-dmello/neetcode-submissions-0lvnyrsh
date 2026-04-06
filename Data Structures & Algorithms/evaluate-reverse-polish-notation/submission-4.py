class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def dfs():
            t = tokens.pop()

            if t not in "+-/*":
                return int(t)

            left = dfs()
            right = dfs()
            
            if t == "+":
                return left + right
            elif t == "-":
                a, b = left, right
                return b - a
            elif t == "*":
                return left*right
            elif t == "/":
                a, b = left, right
                return int(b/a)
                
        return dfs()