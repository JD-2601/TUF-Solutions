class Solution:
    def isPalindrome(self, n):
        rev_n = int(str(n)[::-1])
        return rev_n == n