class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        letters = {}
        for i in s:
            letters[i] = letters.get(i,0) + 1
        for j in t:
            occ = letters.get(j, 0)
            if occ is 0:
                return False
            else:
                letters[j] = letters[j] - 1
        return True
