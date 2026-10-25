class Solution:
    def frequencySort(self, s):
        freq = {}
        for i in s :
            freq[i] = freq.get(i,0) + 1

        res = list(set(s))
        res.sort()
        res.sort(key=freq.get, reverse = True)

        return res
