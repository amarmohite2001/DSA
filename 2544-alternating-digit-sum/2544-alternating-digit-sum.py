class Solution:
    def alternateDigitSum(self, n: int) -> int:
        a = str(n)
        ans=0
        k=0
        for i in a:
            if k&1==0:
                ans+=int(i)
            else:
                ans-=(int(i))
            k+=1
        return ans