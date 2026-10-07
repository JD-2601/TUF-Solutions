class Solution:
    def pattern7(self, n):
        for i in range(n):
            print (' '*(n-i-1),end='')
            print('*'*(2*i+1))