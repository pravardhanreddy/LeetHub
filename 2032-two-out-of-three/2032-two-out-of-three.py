class Solution:
    def twoOutOfThree(self, A: List[int], B: List[int], C: List[int]) -> List[int]:
        set1 = set(A)
        set2 = set()
        for b in set(B):
            if b in set1:
                set2.add(b)
            else:
                set1.add(b)
        for c in set(C):
            if c in set1:
                set2.add(c)
            else:
                set1.add(c)
        return list(set2)
        