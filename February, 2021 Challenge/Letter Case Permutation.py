class Solution:
    def __init__(self):
        self.ans = []
    
    def solve(self, s, idx):
        if idx == len(s):
            self.ans.append(s)
            return
        
        if 'a' <= s[idx] <= 'z' or 'A' <= s[idx] <= 'Z':
            self.solve(s[:idx] + s[idx].upper() + s[idx + 1:], idx + 1)
            self.solve(s[:idx] + s[idx].lower() + s[idx + 1:], idx + 1)
        else:
            self.solve(s, idx + 1)
            
    def letterCasePermutation(self, S: str) -> List[str]:
        self.solve(S, 0)
        return self.ans
