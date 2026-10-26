class Solution:
    def majorityElement(self, nums):
        m = len(nums)//2
        count = {}
        for i in nums :
            if i in count :
                count[i] += 1
            if i not in count :
                count[i] = 1
            if count[i] > m :
                return i
        