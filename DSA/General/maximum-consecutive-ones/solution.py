class Solution:
    def findMaxConsecutiveOnes(self, nums):
        count = 0
        res = 0
        for i in range(len(nums)) :
            if nums[i] == 1:
                count += 1
            if count > res :
                res = count
            if nums[i] == 0 :
                count = 0
        return res




