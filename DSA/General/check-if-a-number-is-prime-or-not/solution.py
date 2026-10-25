class Solution:
    def checkPrime(self, num):
        def check(i) :
            if num == i :
                return True
            if num % i == 0 :
                return False 
            return check(i+1)

        if num < 2 :
            return False
        return check(2)
            