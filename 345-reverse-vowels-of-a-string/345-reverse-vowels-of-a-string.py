import numpy as np
class Solution:
    def reverseVowels(self, s: str) -> str:
        v = []
        for a in s:
            if a in "aeiouAEIOU":
                v.append(a)
        res = ""
        for a in s:
            if a in "aeiouAEIOU":
                res += v.pop()
            else:
                res += a
        return res