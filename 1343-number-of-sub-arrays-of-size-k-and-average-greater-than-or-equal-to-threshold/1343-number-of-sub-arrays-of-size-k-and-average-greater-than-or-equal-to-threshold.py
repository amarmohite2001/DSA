class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        l=0
        r = k-1
        res=0
        curSum = sum(arr[:r+1])
        
        
        while r<len(arr):
            if (curSum/k)>=threshold:
                res+=1
            curSum-=arr[l]
            l+=1
            r+=1
            if r<len(arr):
                curSum+=arr[r]
        return res
                
            
            
        