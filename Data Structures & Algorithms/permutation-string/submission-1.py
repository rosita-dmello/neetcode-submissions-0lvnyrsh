class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        l = 0
        r = len(s1) - 1
        hash_table1 = [0] * 26

        if len(s2) < len(s1):
            return False
        for char in s1:
            ind = ord(char) - ord('a')
            hash_table1[ind] += 1
        
        hash_table2 = [0] * 26

        for i in range(l, r+1):
            let = s2[i]
            ind = ord(let) - ord('a')
            hash_table2[ind] += 1

        if hash_table1 == hash_table2:
                return True
        while r < len(s2) - 1:
            first = s2[l]
            indf = ord(first) - ord('a')
            hash_table2[indf] -= 1
            l += 1
            r += 1
            last = s2[r]
            indl = ord(last) - ord('a')
            hash_table2[indl] += 1

            if hash_table1 == hash_table2:
                return True
        return False
            


            
