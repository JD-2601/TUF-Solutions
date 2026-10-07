class Solution:
    def pattern8(self, n):
        for i in range(n,0,-1):
            print(' '*(n-i),end='')
            print('*'*(2*i-1))