class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        m = 0
        alt = 0
        for i in gain:
            alt += i
            m = max(alt,m)
        return m