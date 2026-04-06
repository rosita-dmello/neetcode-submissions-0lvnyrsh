class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        tally = [0] * 26
        for i in range(len(s)):
            tally[ord(s[i]) - ord('a')] += 1
            tally[ord(t[i]) - ord('a')] -= 1
        for i in tally:
            if i != 0:
                return False
        return True