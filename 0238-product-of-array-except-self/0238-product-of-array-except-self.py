class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1]*len(nums)
        prefix = 1
        postfix = 1
        #for loop to fill all the prefix values and storing it into ans lists
        for i in range(len(nums)):
            ans[i]=prefix
            prefix *= nums[i]
        
        #for loop to fill and multiply the postfix values to the prefix
        for i in range(len(nums)-1,-1,-1):
            ans[i]*=postfix
            postfix*=nums[i]
        
        return ans
            
        
    
        