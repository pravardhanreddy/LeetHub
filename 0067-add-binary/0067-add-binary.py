class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        if len(a) < len(b):
            a, b = b, a
        
        n = len(a) - len(b)
        b = ''.join(['0']*n) + b
        c = 0
        ans = ''
        
        for i in range(len(a)-1, -1, -1):
            s = int(a[i]) + int(b[i]) + c
            ans = str(s%2) + ans
            c = s // 2
        return ans if c == 0 else '1' + ans