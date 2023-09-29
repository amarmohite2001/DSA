class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        curMin,curMax = 0,0
        globMin, globMax = nums[0], nums[0]
        total=0
        for n in nums:
            curMax = max(curMax + n, n)
            curMin = min(curMin + n, n)
            total += n
            globMax = max(curMax, globMax)
            globMin = min(curMin, globMin)

        return max(globMax, total - globMin) if globMax > 0 else globMax
        
        