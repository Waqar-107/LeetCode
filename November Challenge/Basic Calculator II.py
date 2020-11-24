class Solution:
    def calculate(self, s: str) -> int:
        arr = []
        
        curr = None
        for i in range(len(s)):
            if s[i] == " ":
                continue
            
            if '0' <= s[i] <= '9':
                if curr == None:
                    curr = 0
                    
                curr = curr * 10 + ord(s[i]) - ord('0')
            
            else:
                arr.append(curr)
                curr = None
                arr.append(s[i])
            
        if curr != None:
            arr.append(curr)
        
        
        stk = []
        ops = ['+', '-', '*', '/']
        
        i = 0
        while i < len(arr):
            if arr[i] in ops:
                if arr[i] == '+' or arr[i] == '-':
                    stk.append(arr[i])
                    i += 1
                
                else:
                    if arr[i] == '/':
                        stk[-1] //= arr[i + 1]
                    else:
                        stk[-1] *= arr[i + 1]
                    
                    i += 2
            
            else:
                stk.append(arr[i])
                i += 1
        
        ans = stk[0]
        i = 1
        while i < len(stk):
            x = stk[i + 1]
            ch = stk[i]
            
            if ch == '+':
                ans += x
            else:
                ans -= x
            
            i += 2
        
        return ans
                
