class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        length = n ** 2
        ans = [[0 for _ in range(n)] for _ in range(n)]
        
        direction = 'R'
        r = 0
        c = 0
        
        lv = 0
        rv = n - 1
        uv = 0
        dv = n - 1
        
        i = 0
        while i < length:
            if direction == 'R':
                if c <= rv:
                    ans[r][c] = i + 1
                    c += 1
                else:
                    uv += 1
                    c -= 1
                    r += 1
                    direction = 'D'
            
            if direction == 'D':
                if r <= dv:
                    ans[r][c] = i + 1
                    r += 1
                else:
                    rv -= 1
                    r -= 1
                    c -= 1
                    direction = 'L'
            
            if direction == 'L':
                if c >= lv:
                    ans[r][c] = i + 1
                    c -= 1
                else:
                    dv -= 1
                    c += 1
                    r -= 1
                    direction = 'U'
            
            if direction == 'U':
                if r >= uv:
                    ans[r][c] = i + 1
                    r -= 1
                else:
                    lv += 1
                    r += 1
                    c += 1
                    i -= 1
                    direction = 'R'
            i += 1
        
        return ans
                    
