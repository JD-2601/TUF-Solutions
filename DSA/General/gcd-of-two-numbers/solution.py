class Solution:
    def GCD(self, n1, n2):
        
        n = min(n1,n2)
        for i in range(n,0,-1):
            if n1 % i == 0 and n2 % i == 0:
                return i
        