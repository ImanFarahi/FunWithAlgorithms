class Solution(object): 
    def merge(self, intervals):
        if not intervals:
            return intervals
        intervals = sorted(intervals, key=lambda x: x.start)
        res = [intervals[0]]
        for interval in intervals[1:]:
            if res[-1].end >= interval.end:
                continue
            elif res[-1].end >= interval.start:
                res[-1].end = interval.end
            else:
                res.append(interval)
        return res

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

class Solution2(object): 
    def merge(self, intervals):
        if not intervals:
            return intervals
        intervals = sorted(intervals, key=lambda x: x.start)
        res = [intervals[0]]
        for interval in intervals[1:]:
            if res[-1].end >= interval.start:
                res[-1].end = max(res[-1].end, interval.end)
            else:
                res.append(interval)
        return res
 


