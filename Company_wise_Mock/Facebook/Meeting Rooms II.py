class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x : (x[0], x[1]))
        n = len(intervals)
        
        if n == 0:
            return 0
        
        pq = []
        heapq.heappush(pq, intervals[0][1])
        
        ans = 1
        for i in range(1, n):
            while len(pq):
                x = heapq.heappop(pq)
                if x > intervals[i][0]:
                    heapq.heappush(pq, x)
                    break
            
            ans = max(ans, 1 + len(pq))
            heapq.heappush(pq, intervals[i][1])
        
        return ans
