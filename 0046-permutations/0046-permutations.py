class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(first =0):
            if first == len(nums):
                res.append(nums.copy())
            for i in range(first, len(nums)):
                #swaping values at index i and first
                nums[first],nums[i]=nums[i],nums[first]
                #recursively generating permutations for remaining values
                backtrack(first+1)
                #undo the swap to try new permutations
                nums[first],nums[i]=nums[i],nums[first]
        res=[]
        backtrack()
        return res
                
        