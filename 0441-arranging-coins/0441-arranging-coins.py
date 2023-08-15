class Solution:
    def arrangeCoins(self, n: int) -> int:
        res=n
        a=0
        if n == 1:
            return 1
        for i in range(1,n+1):
            if res>=i:
                res -= i
                a+=1
            else:
                return a 
        
            
            
        