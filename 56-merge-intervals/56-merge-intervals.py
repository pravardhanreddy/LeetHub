class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort()
        start, end = intervals[0]
        res = []
        for i in range(1, len(intervals)):
            if end < intervals[i][0]:
                res.append([start, end])
                start, end = intervals[i]
            else:
                end = max(end,intervals[i][1])
        res.append([start, end])
        return res