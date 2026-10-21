class Solution:
    def isPerfect(self, n: int) -> bool:
        res = 0
        for i in range(1,n):
            if n%i == 0:
                res += i
        return res == n
