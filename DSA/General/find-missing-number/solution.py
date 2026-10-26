class Solution:
    def missingNumber(self, nums):
        for i in range(len(nums)+1) :
            num = i
            if num not in nums:
                return num
        