class Solution:
    def pascalTriangleI(self, r, c):
        ans = 1
        n = r - 1
        k = c - 1

        for i in range(k) :
            ans = ans * (n - i) // (i + 1)
        return ans