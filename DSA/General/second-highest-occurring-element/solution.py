class Solution:
    def secondMostFrequentElement(self, nums):
        freq = {}
        for i in nums :
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1

        frequencies = sorted(set(freq.values()), reverse = True)

        if len(frequencies) < 2:
            return -1

        answer = float('inf')
        second_freq = frequencies[1]

        for i in freq:
            if freq[i] == second_freq :
                answer = min(i,answer)
        return answer



