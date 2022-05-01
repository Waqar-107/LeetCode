class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        if n == 0:
            return False
        
        if len(matrix[0]) == 0:
            return False
        
        lo = 0
        hi = len(matrix[0]) * n - 1
        
        while lo <= hi:
            mid = (lo + hi) // 2
            
            r = mid // len(matrix[0])
            c = mid - r * len(matrix[0])
            
            # print(mid, r, c, matrix[r][c])
            
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] > target:
                hi = mid - 1
            else:
                lo = mid + 1
        
        return False
