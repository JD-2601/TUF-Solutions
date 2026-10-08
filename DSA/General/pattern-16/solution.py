class Solution:
    def pattern16(self, n):
        for i in range(n):
            print(chr(65+i)*(i+1))