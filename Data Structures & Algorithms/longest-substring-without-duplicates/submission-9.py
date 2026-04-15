class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        l = 0
        r = 1
        longest = 1
        letters = {s[l]}

        while r < len(s):
            if s[r] in letters:
                while l < r and s[r] in letters: 
                    letters.remove(s[l])
                    l += 1
            else:
                letters.add(s[r])
                r += 1
            longest = max(longest, r-l)

        return longest
                    