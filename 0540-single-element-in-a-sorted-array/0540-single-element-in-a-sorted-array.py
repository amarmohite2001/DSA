class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        i,j=0,1
        while j<len(nums):
            if nums[i]!=nums[j]:
                return nums[i]
            i+=2
            j+=2
        return nums[i]
                
            
        