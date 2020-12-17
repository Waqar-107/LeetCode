class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        uno = defaultdict(int)
        dos = defaultdict(int)
        
        for a in A:
            for b in B:
                uno[a + b] += 1
        
        for c in C:
            for d in D:
                dos[c + d] += 1
        
        ans = 0
        for key in uno:
            # c + d = 0 - a - b = -(a + b)
            ans += uno[key] * dos[-key]
        
        return ans
