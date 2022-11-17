class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if os.path.commonprefix(strs):
            return os.path.commonprefix(strs)
        else:
            return ""
        