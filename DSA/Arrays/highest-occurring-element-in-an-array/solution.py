class Solution:
    def mostFrequentElement(self, nums):
        freq = {}
        for i in nums:
            if i in freq :
                freq[i] += 1
            else:
                freq[i] = 1


        max_count = 0
        answer = nums[0]
        for i in freq :
            if freq[i] > max_count :
                max_count = freq[i]
                answer = i
            elif freq[i] == max_count and i < answer :
                answer = i
        return answer
