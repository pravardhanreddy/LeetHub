class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prevneg = -100
        prevmax = prevneg
        maxtillnow = 1
        maxoverall = nums[0]
        pos = True
        become1 = False
        for n in nums:
            if n > 0:
                maxtillnow *= n
            elif n == 0:
                maxtillnow = 1
                pos = True
            else:
                if pos:
                    prevneg = n
                    prevmax = maxtillnow
                    maxtillnow = 1
                    pos = False
                else:
                    maxtillnow = maxtillnow * prevneg * n * prevmax
                    if not become1 and maxtillnow == 1:
                        become1 = True
                    pos = True
            maxoverall = max(maxtillnow, maxoverall) if maxtillnow != 1 else max(maxoverall, n)
        ans1 = maxoverall if not become1 else max(maxoverall, 1)
        
        prevneg = -100
        prevmax = prevneg
        maxtillnow = 1
        maxoverall = nums[0]
        pos = True
        become1 = False
        for n in reversed(nums):
            if n > 0:
                maxtillnow *= n
            elif n == 0:
                maxtillnow = 1
                pos = True
            else:
                if pos:
                    prevneg = n
                    prevmax = maxtillnow
                    maxtillnow = 1
                    pos = False
                else:
                    maxtillnow = maxtillnow * prevneg * n * prevmax
                    if not become1 and maxtillnow == 1:
                        become1 = True
                    pos = True
            maxoverall = max(maxtillnow, maxoverall) if maxtillnow != 1 else max(maxoverall, n)
        ans2 = maxoverall if not become1 else max(maxoverall, 1)
        
        return max(ans1, ans2)
