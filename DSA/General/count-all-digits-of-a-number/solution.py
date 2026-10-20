class Solution:
    def countDigit(self, n):
        count=0
        for i in range (len(str(n))):
            count+=1
        return count