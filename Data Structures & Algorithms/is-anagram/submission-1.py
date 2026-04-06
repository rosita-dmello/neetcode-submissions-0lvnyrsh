class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freqs = {}
        freqt = {}
        for letter in s:
            freqs[letter] = freqs.get(letter, 0) + 1
        for letter in t:
            freqt[letter] = freqt.get(letter, 0) + 1
        return freqs == freqt
        