class Solution:
    def addBinary(self, a: str, b: str) -> str:
        d=int(a,2)
        c=int(b,2)
        x=d+c
        return bin(x)[2:]
        