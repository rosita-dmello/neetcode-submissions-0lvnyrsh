class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        l, r = 0, 0
        maxfreq = 0
        ans = 0

        for r in range(len(s)):
            char = s[r]

            count[char] += 1
            maxfreq = max(maxfreq, count[char])

            while ((r - l + 1) - maxfreq) > k:
                count[s[l]] -= 1
                l += 1
            
            ans = max(ans, r-l+1)
        return ans
            