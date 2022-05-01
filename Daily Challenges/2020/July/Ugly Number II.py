class Solution:
    def nthUglyNumber(self, n: int) -> int:
        u = [0] * (n + 1)
        u[1] = 1
        
        i2, i3, i5 = 1, 1, 1
        m2, m3, m5 = 2, 3, 5
        
        for i in range(2, n + 1):
            u[i] = min(m2, m3, m5)
            
            if u[i] == m2:
                i2 += 1
                m2 = u[i2] * 2
                
            if u[i] == m3:
                i3 += 1
                m3 = u[i3] * 3
                
            if u[i] == m5:
                i5 += 1
                m5 = u[i5] * 5
                
        return u[n]
