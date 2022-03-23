class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        
        
        if startValue >= target:
            return startValue - target
        
        count = 0
        
        while startValue < target:
            count += 1
            startValue *= 2
        
        rem = startValue - target
        
        p = count
        while p > 0:
            if rem == 0:
                break
            else:
                count += rem//(2**p)
                rem = rem % (2**p)
                p -= 1
        return count + rem
            
            