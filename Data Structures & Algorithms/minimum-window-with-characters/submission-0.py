class Solution:
    
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        l = 0
        
        hasht, hashs = {}, {}

        for c in t:
            hasht[c] = 1 + hasht.get(c, 0)

        have = 0
        need = len(hasht)
        rl, rr = [-1, -1]
        rlen = float("infinity")
        for r in range(len(s)):
            char = s[r]
            hashs[char] = 1 + hashs.get(char, 0)
            if char in hasht and hasht[char] == hashs[char]:
                have += 1
            
            while have == need:
                if (r - l + 1) < rlen:
                    rlen = r - l + 1
                    rl, rr = l, r
                hashs[s[l]] -= 1    
                if s[l] in hasht and hashs[s[l]] < hasht[s[l]]:
                    have -= 1
                l += 1
        l, r = rl, rr
        return s[l:r+1] if l > -1 else ""
            



            
