class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        n = len(mat)
        m = len(mat[0])
        
        for i in range(n - 1, -1, -1):
            c = 0
            r = i
            temp = []
            while c < m and r < n:
                temp.append(mat[r][c])
                c += 1
                r += 1
            
            temp.sort()
            
            c = 0
            r = i
            while c < m and r < n:
                mat[r][c] = temp[c]
                r += 1
                c += 1
        
        for i in range(1, m):
            temp = []
            c = i
            r = 0
            while c < m and r < n:
                temp.append(mat[r][c])
                r += 1
                c += 1
            
            temp.sort()
            
            c = i
            r = 0
            while c < m and r < n:
                mat[r][c] = temp[r]
                c += 1
                r += 1
        
        return mat
                
