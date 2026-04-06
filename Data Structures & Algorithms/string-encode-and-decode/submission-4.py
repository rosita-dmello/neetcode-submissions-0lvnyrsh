class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ''
        for string in strs:
            encoded = encoded + str(len(string))  + '#' + string
        return encoded
    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            curr_len = 0
            curr_string = ''
            j = i
            while s[j] != '#':
                j = j + 1
            curr_len = int(s[i:j])
            i = j + 1
            j = j + curr_len
            curr_string = s[i:j+1]
            result.append(curr_string)
            i = j + 1
        return result