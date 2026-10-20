class Solution:
    def largestDigit(self, n):
        largest_dig = 0
        for i in str(n):
            if int(i) > largest_dig :
                largest_dig = int(i)
        return largest_dig