class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n ==1:
            return 1
        F1=0
        F2=1
        i=2
        while i<=n:
            temp=F1+F2
            F1=F2
            F2=temp
            i+=1
        return temp
            
        
    
    
        