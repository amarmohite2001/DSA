class Solution:
    def isHappy(self, n: int) -> bool:
        while(len(str(n))>1):
            temp=0
            for x in str(n):
                temp+=int(x)**2
            n=temp
        
        if n!=1 and n!=7:
            return False
        else:
            return True
            
                
        