class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum=nums[0]
        curSum=0
        for i in nums:
            if curSum<0:
                curSum=0
            curSum+=i
            if maxSum<curSum:
                maxSum=curSum
                
            # maxSum = max(maxSum, curSum)
        return maxSum
        