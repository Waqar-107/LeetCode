class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: (x[1], x[0]))
        
        ans = 0
        last = -99999999999
        
        n = len(points)
        for i in range(n):
            if points[i][0] <= last <= points[i][1]:
                continue
            
            ans += 1
            last = points[i][1]
        
        return ans
        
