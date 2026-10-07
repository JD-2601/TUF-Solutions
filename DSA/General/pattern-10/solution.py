class Solution:
    def pattern10(self, n):
        for i in range(1,n):
            print('*'*i)
        for j in range(n,0,-1):
            print('*'*j)
