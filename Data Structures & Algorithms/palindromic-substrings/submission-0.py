class Solution:
    def countSubstrings(self, s: str) -> int:
        total_res = 0
        for i in range(len(s)):
            odd = self.count_palindromes(i, i, s)
            even = self.count_palindromes(i, i+1, s)
            total_res = total_res + odd + even
        return total_res
        
        
    def count_palindromes(self, l, r, s):
        res = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            res += 1
            l -= 1
            r += 1

        return res
            