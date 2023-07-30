# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 0, n
        while left<=right:
            if n == 1:
                return n     
            mid = (left+right)//2
            if isBadVersion(mid)==False:
                left=mid+1
                if isBadVersion(left)==True:
                    return left
            else:
                right=mid-1
        return left
                
                