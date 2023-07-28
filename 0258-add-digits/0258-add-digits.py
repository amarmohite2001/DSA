class Solution:
    def addDigits(self, num: int) -> int:
        while(len(str(num))>1):
            temp=0
            for x in str(num):
                temp+=int(x)
            num=temp
        return num
        