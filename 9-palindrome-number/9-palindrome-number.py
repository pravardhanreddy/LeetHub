class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        l = len(x)-1
        i = 0
        while(i<l):
            if x[i] != x[l]:
                return False
            i += 1
            l -= 1
        return True
        