class Solution:
    def pascalTriangleIII(self, n):
        ans = []
        for r in range(1,n+1) :
            row = [1]
            num = 1
            for i in range(1,r) :
                num = num * (r-i) // i
                row.append(num)
            ans.append(row)
        return ans

