class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        n = len(s)
        
        if n < k:
            return False
        
        temp = ""
        dict = {}
        
        for i in range(k):
            temp += s[i]
            
        dict[temp] = True
        
        for i in range(k, n):
            temp = temp[1:]
            temp += s[i]

            dict[temp] = True
        
        return len(dict.keys()) == pow(2, k)
