class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # i,j=0,1
        # while i<=j and j<len(nums):
        #     if nums[i]==nums[j]:
        #         j+=1
        #     else:
        #         nums[i+1]=nums[j]
        #         i+=1
        # return i+1
        
        k=1
        for i in range(1,len(nums)):
            if nums[i]!= nums[i-1]:
                nums[k]=nums[i]
                k+=1
        return k
            
        