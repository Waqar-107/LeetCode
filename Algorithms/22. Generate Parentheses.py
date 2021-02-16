class Solution:
    def __init__(self):
        self.ans = []
    
    def regular(self, s):
        cnt = 0
        for i in range(len(s)):
            if s[i] == '(':
                cnt += 1
            else:
                if cnt:
                    cnt -= 1
                else:
                    return False
                
        if cnt == 0:
            return True
        return False
    
    def solve(self, s, idx):
        if idx == len(s) - 1:
            if self.regular(s):
                self.ans.append(s)
            return
        
        self.solve(s[:idx] + '(' + s[idx + 1:], idx + 1)
        self.solve(s[:idx] + ')' + s[idx + 1:], idx + 1)
        
    def generateParenthesis(self, n: int) -> List[str]:
        s = "(" + ((n - 1) * 2) * '#' + ")"
        
        self.solve(s, 1)
        
        return self.ans
