class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = [str(i) for i in digits]
        res = int("".join(s))
        temp =str(res+1)
        return [int(temp[i]) for i in range(len(temp))]
        
        