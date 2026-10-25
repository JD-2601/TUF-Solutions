class Solution:    
    def palindromeCheck(self, s):
        if len(s) <=1 :
            return True
        if s[0] != s[-1] :
            return False
        return self.palindromeCheck(s[1:-1])