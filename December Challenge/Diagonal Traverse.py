class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix)
        if n == 0:
            return []
        m = len(matrix[0])
        
        ans = []
        direction = 1
        
        for i in range(m):
            r = 0
            c = i
            temp = []
            while c >= 0 and r < n:
                temp.append(matrix[r][c])
                r += 1
                c -= 1

            if direction:
                temp = temp[::-1]
            
            direction = 1 - direction
            ans = ans + temp
        
        for i in range(1, n):
            r = i
            c = m - 1
            
            temp = []
            while c >= 0 and r < n:
                temp.append(matrix[r][c])
                r += 1
                c -= 1
                
            if direction:
                temp = temp[::-1]
            
            direction = 1 - direction
            ans = ans + temp
        
        return ans
                
