class Solution:
    def primeUptoN(self, n):
        prime_nums = 0
        if n < 2:
            return 0
        for i in range(2,n+1):
            is_prime = True
            for j in range(2,i):
                if i % j == 0:
                    is_prime= False
                    break
            if is_prime :
                prime_nums += 1
        return prime_nums

