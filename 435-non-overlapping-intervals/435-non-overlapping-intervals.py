class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[0])
        res = 0
        end = intervals[0][1]
        for i in range(1,len(intervals)):
            if intervals[i][0] < end:
                res += 1
                end = min(end, intervals[i][1])
            else:
                end = intervals[i][1]
        return res
        