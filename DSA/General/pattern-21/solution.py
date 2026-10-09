class Solution:
    def pattern21(self, n):
        if n==1:
            print('*')
        else:
        
        
            print('*'*n,end='')
            print()

            for j in range(1,n-1):
                print('*',end='')
                print(' '*(n-2),end='')
                print('*')
          

            print('*'*n,end='')
                
        