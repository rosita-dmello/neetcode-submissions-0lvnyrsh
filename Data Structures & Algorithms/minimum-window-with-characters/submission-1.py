class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count_t = defaultdict(int)
        count_win = defaultdict(int)

        for c in t:
            count_t[c] += 1

        have = 0
        need = len(count_t)

        l = 0
        r = 0
        res = [-1, -1]
        m_len = float("infinity")

        for r in range(len(s)):
            count_win[s[r]] += 1
            if count_win[s[r]] == count_t[s[r]]:
                have += 1
            while have == need:
                if r-l+1 < m_len:
                    m_len = r-l+1
                    res = [l, r]
                count_win[s[l]] -= 1
                if s[l] in count_t and count_win[s[l]] < count_t[s[l]]:
                    have -= 1
                l += 1

        return s[res[0]:res[1]+1] if m_len != float("infinity") else ""
        
            
