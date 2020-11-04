class Solution:
    def mult(self, num, digit):
        carry = 0
        ans = ""
        for i in range(len(num) - 1, -1, -1):
            x = (ord(digit) - ord("0")) * (ord(num[i]) - ord("0")) + carry
            
            ans += chr(x % 10 + ord("0"))
            carry = x // 10
        if carry > 0:
            ans += chr(carry + ord("0"))
        return ans[::-1]
    
    def multiply(self, num1: str, num2: str) -> str:
        if len(num1) < len(num2):
            num1, num2 = num1, num2
        
        layers = []
        shift = 0
        for i in range(len(num2) - 1, -1, -1):
            x = self.mult(num1, num2[i])
            for j in range(shift):
                x += "0"
            
            shift += 1
            layers.append(x)
        
        mx = 0
        for l in layers:
            mx = max(mx, len(l))
        
        for i in range(len(layers)):
            while len(layers[i]) < mx:
                layers[i] = "0" + layers[i]
        
        carry = 0
        ans = ""
        for i in range(mx - 1, -1, -1):
            cnt = 0
            for l in layers:
                cnt += (ord(l[i]) - ord("0"))
            
            cnt += carry
            ans += chr(cnt % 10 + ord("0"))
            carry = cnt // 10
        
        if carry:
            ans += chr(carry + ord("0"))
        
        ans = ans[::-1]
        while len(ans) and ans[0] == "0":
            ans = ans[1:]
        
        if len(ans) == 0:
            return "0"
        return ans
