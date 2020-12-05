class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factors = []
        sq = int(math.sqrt(n)) + 1
        
        for i in range(1, sq):
            if n % i == 0:
                factors.append(i)
                if n // i != i:
                    factors.append(n // i)
        
        factors.sort()
        
        if len(factors) < k:
            return -1
        
        return factors[k - 1]
        
