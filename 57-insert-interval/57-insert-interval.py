class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        l, r = 0, len(intervals) - 1
        while r-l > 1:
            mid = (l+r)//2
            if newInterval[0] == intervals[mid][0]:
                l = mid
                break
            if newInterval[0] > intervals[mid][0]:
                l = mid
            else:
                r = mid
        # append case
        if intervals[r][1] < newInterval[0]:
            intervals.insert(r+1, newInterval)
            return intervals
        if intervals[l][1] < newInterval[0] and (l+1 == len(intervals) or newInterval[1] < intervals[l+1][0]):
            intervals.insert(l+1, newInterval)
            return intervals
        
        # merge case
        if intervals[l][1] < newInterval[0]: # ignore
            l += 1
        
        r = l
        while r < len(intervals) and intervals[r][1] < newInterval[1]:
            r += 1
        if r == len(intervals) or intervals[r][0] > newInterval[1]:
            r -= 1
        start = min(intervals[l][0], newInterval[0])
        end = max(intervals[r][1], newInterval[1])
        if r < 0:
            end = newInterval[1]
        newList = []
        newList.extend(intervals[:l])
        newList.append([start, end])
        newList.extend(intervals[r+1:])
        return newList