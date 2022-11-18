class Solution:
    def addBinary(self, a: str, b: str) -> str:
        c,d=int(b,2),int(a,2)
        # x=d+c
        return bin(c+d)[2:]
        