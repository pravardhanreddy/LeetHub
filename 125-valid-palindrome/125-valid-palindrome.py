class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) -1
        while l < r:
            if not ((0 <= ord(s[l]) - ord('a') < 26) or (0 <= ord(s[l]) - ord('A') < 26) or (ord('0') <= ord(s[l]) <= ord('9'))):
                l += 1
                continue
            if not ((0 <= ord(s[r]) - ord('a') < 26) or (0 <= ord(s[r]) - ord('A') < 26) or (ord('0') <= ord(s[r]) <= ord('9'))):
                r -= 1
                continue
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True
        