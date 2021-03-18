class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        intervals.sort(key = lambda x : (x[1], x[0]))
        
        if n == 0:
            return 0
        
        ans = [intervals[0]]
        for i in range(1, n):
            if intervals[i][0] >= ans[-1][1]:
                ans.append(intervals[i])
        
        return n - len(ans)
