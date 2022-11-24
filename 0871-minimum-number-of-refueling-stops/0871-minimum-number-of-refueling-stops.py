import heapq
class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        missed = []
        stations.append([target, 0])
        cnt = 0
        fuel = startFuel
        for i, (position, gas) in enumerate(stations):
            while fuel < position and len(missed):
                cnt += 1
                fuel += -heapq.heappop(missed)
            if fuel < position:
                return -1
            heapq.heappush(missed, -gas)

        return cnt
            
