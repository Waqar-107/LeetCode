class Solution:
    def addBinary(self, a: str, b: str) -> str:
        while len(a) < len(b):
            a = '0' + a
        
        while len(b) < len(a):
            b = '0' + b
        
        n = len(a) - 1
        carry = 0
        ans = []
        
        print(a, b)
        for i in range(n, -1, -1):
            s = int(a[i]) + int(b[i])
            
            if s == 0:
                ans.append(str(carry))
                carry = 0
            elif s == 1:
                if carry:
                    ans.append('0')
                else:
                    ans.append('1')
                    carry = 0
            else:
                if carry:
                    ans.append('1')
                else:
                    ans.append('0')
                    
                carry = 1
        
        if carry:
            ans.append('1')
            
        ans = ans[::-1]
        return "".join(ans)
