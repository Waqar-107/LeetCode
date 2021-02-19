class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        n = len(s)
        cut = [False] * n
        
        for i in range(n):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == ')':
                if len(stack):
                    stack.pop()
                else:
                    cut[i] = True
        
        for i in range(len(stack)):
            cut[stack[i]] = True
        
        ans = ""
        for i in range(n):
            if not cut[i]:
                ans += s[i]
        
        return ans
