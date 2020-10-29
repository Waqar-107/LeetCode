class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        n = len(seats)
        left = [0] * n
        right = [0] * n
        
        dist = 0
        for i in range(n):
            left[i] = dist
            
            if seats[i] == 1:
                dist = 1
            else:
                dist += 1
        
        dist = 0
        for i in range(n - 1, -1, -1):
            right[i] = dist
            
            if seats[i] == 1:
                dist = 1
            else:
                dist += 1
        
        ans = 0
        
        # first and last index
        if seats[0] == 0:
            ans = max(ans, right[0])
        if seats[-1] == 0:
            ans = max(ans, left[-1])
        
        for i in range(1, n - 1, 1):
            if seats[i] == 0:
                ans = max(ans, min(left[i], right[i]))
        
        return ans
