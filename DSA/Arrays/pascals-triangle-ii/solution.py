class Solution:
    def pascalTriangleII(self, r):
        ans = []
        num = 1
        ans.append(num)

        for i in range(1,r) :
            num = num * (r - i) // i 
            ans.append(num)
        return ans