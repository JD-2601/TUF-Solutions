class Solution:
    def maxSubArray(self, nums):
        
        largest_sum = float('-inf')
        current_sum = 0

        for i in range(len(nums)):
            current_sum += nums[i]

            largest_sum = max(largest_sum, current_sum)

            if current_sum < 0:
                current_sum = 0

        return largest_sum