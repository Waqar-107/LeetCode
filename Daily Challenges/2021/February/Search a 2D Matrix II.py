class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for lst in matrix:
            for l in lst:
                if l == target:
                    return True
                
        
        return False
