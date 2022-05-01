class Solution:
    def __init__(self):
        self.ans = set()
    
    def solve(self, idx, n, k, s):
        if idx == n:
            self.ans.add(int(s))
            return
        
        if int(s[idx - 1]) + k <= 9:
            self.solve(idx + 1, n, k, s + str(int(s[idx - 1]) + k))
            
        if int(s[idx - 1]) - k >= 0:
            self.solve(idx + 1, n, k, s + str(int(s[idx - 1]) - k))
            
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        for i in range(1, 10):
            self.solve(1, n, k, str(i))
            
        return list(self.ans)
        
