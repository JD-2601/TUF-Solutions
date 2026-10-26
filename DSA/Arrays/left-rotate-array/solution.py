class Solution:
    def rotateArray(self, nums, k: int) -> None:
         m = len(nums)
         k = k % m
         nums[:] = nums[k : ] + nums[0 : k]
