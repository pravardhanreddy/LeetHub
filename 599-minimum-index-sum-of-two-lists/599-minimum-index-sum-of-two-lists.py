class Solution:
    def findRestaurant(self, A: List[str], B: List[str]) -> List[str]:
        if len(B) < len(A):
            A, B = B, A
        d = dict()
        ans = []
        mi = len(A) + len(B)
        for i in range(len(A)):
            d[A[i]] = i
        for i in range(len(B)):
            if B[i] in d:
                ind = i + d[B[i]]
                if ind < mi:
                    mi = ind
                    ans = [B[i]]
                elif ind == mi:
                    ans.append(B[i])
        return ans