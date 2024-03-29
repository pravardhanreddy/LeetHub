import heapq
class MedianFinder:

    def __init__(self):
        self.small, self.large = [], []

    def addNum(self, num: int) -> None:
        
        heapq.heappush(self.small, -num)
        
        
            
        # make sure order is satisfied
        if self.small and self.large and -self.small[0] > self.large[0]:
            heapq.heappush(self.large, -heapq.heappop(self.small))
            if len(self.large) > len(self.small) + 1:
                heapq.heappush(self.small, -heapq.heappop(self.large))
            
        # make sure len is approx equal
        
        if len(self.small) > len(self.large) + 1:
            heapq.heappush(self.large, -heapq.heappop(self.small))

        

    def findMedian(self) -> float:
        s, l = len(self.small), len(self.large)
        if (s+l) % 2:
            if s > l:
                return -self.small[0]
            return self.large[0]
        
        return (self.large[0] - self.small[0])/2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()