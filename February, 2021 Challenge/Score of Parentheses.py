class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        stack = [0]
        
        ans = 0
        for c in S:
            if c == '(':
                stack.append(0)
            
            else:
                v = stack[-1]
                stack.pop()
                stack[-1] += max(2 * v, 1)
        
        return stack[-1]
