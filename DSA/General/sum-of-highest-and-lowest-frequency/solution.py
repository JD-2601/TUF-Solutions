class Solution:
    def sumHighestAndLowestFrequency(self, nums):
        freq = {}
        for i in nums :
            if i in freq :
                freq[i] += 1
            else:
                freq[i] = 1
        frequencies = sorted(freq.values())
        sum_high_low = frequencies[0] + frequencies[-1]
        return sum_high_low

