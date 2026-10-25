class Solution:
    def addDigits(self, num):
        if num < 10 :
            return num
        total = 0
        while num > 0 :
            total += num % 10
            num //= 10
        return self.addDigits(total)
