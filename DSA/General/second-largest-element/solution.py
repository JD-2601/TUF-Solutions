class Solution:
    def secondLargestElement(self, nums):
        largest = nums[0]
        second_largest = float('-inf')
        for i in range(1,len(nums)) :
            if nums[i] > largest :
                second_largest = largest
                largest = nums[i]
            elif nums[i] < largest and nums[i] > second_largest :
                second_largest = nums[i] 
        if second_largest > float('-inf') :
            return second_largest
        else:
            return -1