class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        chars = []
        
        for i in range(len(S)):
            if "a" <= S[i] <= "z" or "A" <= S[i] <= "Z":
                chars.append(S[i])
        
        chars = chars[::-1]
        idx = 0
        ans = ""
        
        for i in range(len(S)):
            if "a" <= S[i] <= "z" or "A" <= S[i] <= "Z":
                ans += chars[idx]
                idx += 1
            else:
                ans += S[i]
        
        return ans
