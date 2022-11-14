class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        sarr= s.strip().split(" ")
        return len(sarr[-1])