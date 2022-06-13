class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n == 0:
            return 0
        l = []
        l.append(0)
        l.append(1)
        for i in range(2,n+1):
            if i % 2 == 0:
                l.append(l[i//2])
            else:
                l.append(l[(i-1)//2] + l[(i+1)//2])
        return max(l)