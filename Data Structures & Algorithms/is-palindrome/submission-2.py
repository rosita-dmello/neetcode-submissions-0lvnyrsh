class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_ = ''.join([l.lower() for l in s if l.isalnum()])
        print(s_)
        n = len(s_)
        i = 0
        j = n-1
        
        while i < j and s_ != "":
            if s_[i] != s_[j]:
                return False
            else:
                i+=1
                j-=1
        return True