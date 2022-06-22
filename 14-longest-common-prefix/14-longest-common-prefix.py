class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        com = strs[0]
        for i in range(1,len(strs)):
            j = 0
            while j < (min(len(com), len(strs[i]))):
                if com[j] != strs[i][j]:
                    break
                j += 1
            if j == 0:
                return ""
            com = com[:j]
        return com