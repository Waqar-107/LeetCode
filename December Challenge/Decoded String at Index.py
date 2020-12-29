class Solution:
    def decodeAtIndex(self, S: str, K: int) -> str:
        sz = 0
        for i in range(len(S)):
            if S[i].isdigit():
                sz *= int(S[i])
            else:
                sz += 1
        
        for c in reversed(S):
            K %= sz
            
            if K == 0 and c.isalpha():
                return c
            
            if c.isdigit():
                sz /= int(c)
            else:
                sz -= 1
