class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x : (x[0], x[1]))
        
        ans = []
        n = len(intervals)
        
        for i in range(n):
            if len(ans) == 0:
                ans.append(intervals[i])
            
            else:
                if ans[-1][0] <= intervals[i][0] and intervals[i][1] <= ans[-1][1]:
                    continue
                
                elif ans[-1][1] >= intervals[i][0]:
                    ans[-1][1] = max(ans[-1][1], intervals[i][1])
                
                else:
                    ans.append(intervals[i])
        
        return ans
        
