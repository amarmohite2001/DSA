class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        a = [i for i in range(len(nums)+1)]
        # print(sum(a))
        # print(sum(nums))
        return sum(a)-sum(nums)
        