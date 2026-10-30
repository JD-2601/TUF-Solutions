class Solution:
    def majorityElementTwo(self, nums):
        seen = {}
        res = []
        n = len(nums)
        for i in nums :
            if i not in seen :
                seen[i] = 1
            else :
                seen[i] += 1
        for i in seen :
            if seen[i] > n/3 :
                res.append(i)
        return res

        