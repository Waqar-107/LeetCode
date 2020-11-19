class Solution:
    def decodeString(self, s: str) -> str:
        num = 0
        stack = [""]
        
        n = len(s)
        for i in range(n):
            if "0" <= s[i] <= "9":
                num = num * 10 + (ord(s[i]) - ord('0'))
            
            elif "a" <= s[i] <= "z":
                if num:
                    stack.append(num)
                    num = 0
                    stack.append("")
                    
                stack[-1] += s[i]
            
            elif s[i] == "[":
                stack.append(num)
                num = 0
                stack.append("")
            
            else:
                m = len(stack)
                stack[m - 3] += stack[m - 2] * stack[m - 1]
                stack.pop()
                stack.pop()
                
        return stack[0]
