class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        l,r = 0,1
        #>,=,< = 1, 0 ,-1
        res, prev = 1, ""
        while r<len(arr):
            if arr[r-1]>arr[r] and prev !=1:
                if res<(r-l+1):
                    res = r-l+1
                # res = max(res, r-l+1)
                r+=1
                prev=1
            elif arr[r-1]<arr[r] and prev != -1:
                if res<(r-l+1):
                    res = r-l+1
                # res = max(res, r-l+1)
                r+=1
                prev=-1
            else:
                r = r+1 if arr[r]==arr[r-1] else r
                l=r-1
                prev=0
        return res
        