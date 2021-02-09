class Solution:
    def convert(self, s: str, numRows: int) -> str:
        n = len(s)
        idx = defaultdict(list)
        
        r = 0
        flag = 1
        
        for i in range(n):
            idx[r].append(s[i])
            
            r += flag
            if r == numRows:
                flag = -1
                r = numRows - 2
            if r == -1:
                flag = 1
                r = 1
        
        ans = ""
        arr = list(idx.keys())
        arr.sort()
        
        for key in arr:
            ans += "".join(idx[key])
            
        return ans
                
                
