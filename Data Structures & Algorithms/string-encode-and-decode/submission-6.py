class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ''
        for s in strs:
            encoded = encoded + str(len(s)) + '#' + s

        return encoded
    def decode(self, s: str) -> List[str]:
        i = 0 
        j = 0
        res = []
        while j < len(s):
            while s[j] != '#':
                j+=1
            
            length = int(s[i:j])

            i = j+1
            j = j + length + 1

            res.append(s[i:j])
            i = j
        return res

        # "5#hello"
        

