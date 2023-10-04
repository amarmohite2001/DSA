class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        length = float("inf")
        sumcur = 0
        l=0
        for r in range(len(nums)):
            sumcur += nums[r]
            while sumcur>=target:
                length = min(r-l+1, length)
                sumcur -= nums[l]
                l+=1
        return 0 if length == float("inf") else length
                
            
        