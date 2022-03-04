class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        s = 1 if x>= 0 else -1
        rev = s * int(str(abs(x))[::-1])
        if -1*(2**31) < rev < (2**31)-1:
            return rev
        else:
            return 0