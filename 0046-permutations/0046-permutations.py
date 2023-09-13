class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(curr):
            if len(curr) == len(nums):
                res.append(curr.copy())
                return
            for num in nums:
                if num not in curr:
                  #swaping values at index i and first
                  curr.append(num)
                  #recursively generating permutations for remaining values
                  backtrack(curr)
                  #undo the swap to try new permutations
                  curr.pop()
        res=[]
        # temp=[]
        backtrack([])
        return res
                
        