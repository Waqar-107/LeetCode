class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        forward_by_min = (5 * minutes) / 60
        
        if hour == 12:
            h = 0
        else:
            h = hour * 5
            
        h += forward_by_min
        
        return min(abs(h - minutes) * 6, 360 - abs(h - minutes) * 6)
