class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
    
        letter_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        res = []
        

        def dfs(i, substring):
            if i == len(digits):
                res.append(substring)
                return
            
            poss = letter_map[digits[i]]
            for j in range(len(poss)):
                dfs(i+1, substring + poss[j])
        if digits:
            dfs(0, '')
        return res


