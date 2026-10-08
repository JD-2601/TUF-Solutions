class Solution:
    def pattern18(self, n):
        for i in range (1,n+1):
            for j in range(n-i,n):
                print(chr(65+j),end=' ')
            print()