class Solution:
    def reverseArray(self, nums):
        if len(nums) == 0 :
            return []
        return [nums[-1]] + self.reverseArray(nums[:-1])