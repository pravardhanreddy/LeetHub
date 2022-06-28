from collections import Counter
class Solution:
        
    def minDeletions(self, s: str) -> int:
        c = Counter(s)
        print(c)
        bag = set()
        ans = 0
        for _, count in c.items():
            while count != 0 and count in bag:
                count -= 1
                ans += 1
            bag.add(count)
        return ans