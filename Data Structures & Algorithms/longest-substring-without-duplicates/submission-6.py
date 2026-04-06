class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        indices = {}
        l = 0
        r = 0
        longest = 0
        
        for r in range(len(s)):
            char = s[r]
            if char in indices:
                l = max(indices[char] + 1,l)
            indices[char] = r
            longest = max(longest, r-l+1) 
        return longest

        