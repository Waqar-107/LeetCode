class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        curr = 0
        k = 0
        
        while curr < target:
            curr += k
            k += 1
            
        while (curr - target) % 2:
            curr += k
            k += 1
        
        return k - 1
        
