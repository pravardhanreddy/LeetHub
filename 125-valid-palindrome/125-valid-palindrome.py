class Solution:
    def isPalindrome(self, s: str) -> bool:
        ans = []
        s = s.lower()
        for char in s:
            if (0 <= ord(char) - ord('a') < 26) or (ord('0') <= ord(char) <= ord('9')):
                ans.append(char)
        for i in range(len(ans)):
            if ans[i] != ans[len(ans) - i - 1]:
                return False
        return True
        