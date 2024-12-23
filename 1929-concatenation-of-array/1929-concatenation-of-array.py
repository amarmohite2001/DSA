class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n=len(nums)
        ans=nums.copy()
        ans.extend(nums)
        # print(ans)
        # for i in range(len(nums)):
        #     ans[i]=nums[i]
        #     ans[i+n]=nums[i]
        return ans