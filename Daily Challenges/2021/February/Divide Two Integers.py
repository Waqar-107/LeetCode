class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        d = abs(dividend) // abs(divisor)
        
        if dividend < 0 and divisor > 0:
            d *= -1
        elif dividend > 0 and divisor < 0:
            d *= -1
        
        if d > pow(2, 31) - 1:
            d = pow(2, 31) - 1
        
        if d < -pow(2, 31):
            d = -pow(2, 31)
            
        return d
