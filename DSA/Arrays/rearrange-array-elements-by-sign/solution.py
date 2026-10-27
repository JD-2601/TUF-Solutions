class Solution:
    def rearrangeArray(self, nums):
        neg = []
        pos = []
        for i in nums :
            if i > 0 :
                pos.append(i)
            else :
                neg.append(i)
        for j in range(len(nums)//2) :
            nums[j*2] = pos[j]
            nums[j*2+1] = neg[j]
            
        return nums