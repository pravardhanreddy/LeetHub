class Solution:
    def longestPalindrome(self, A: str) -> str:
        m = 0
        ans = ''
        for i in range(len(A)):
            # case odd
            ln = 1
            while i - ln >=0 and i + ln < len(A) and A[i-ln] == A[i+ln]:
                ln += 1
            ln -= 1
            if m < 2*ln+1:
                m = 2*ln+1
                ans = A[i-ln:i+ln+1]
            # case even
            ln = 1
            while i - ln + 1 >=0 and i + ln < len(A) and A[i-ln+1] == A[i+ln]:
                ln += 1
            ln -= 1
            if m < 2*ln:
                m = 2*ln
                ans = A[i-ln+1:i+ln+1]
        return ans if len(ans) != 0 else A[0]