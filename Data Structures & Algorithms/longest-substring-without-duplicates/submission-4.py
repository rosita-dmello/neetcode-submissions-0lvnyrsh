class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        curr = 0
        
        l = 0
        r = 0
        letters = set()

        for r in range(0, len(s)):
            char = s[r]
            while char in letters:
                letters.remove(s[l])
                l = l+1
            letters.add(char)
            curr = len(letters)
            longest = max(curr, longest)
            

        return longest
