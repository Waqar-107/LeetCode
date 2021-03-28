class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        seen = {}
        rep = -1
        cells_backup = [c for c in cells]
        
        for i in range(n):
            cells2 = [0] * 8
            for j in range(1, 7):
                cells2[j] = 1 - (cells[j - 1] ^ cells[j + 1])
            
            cl = ""
            for j in range(8):
                cells[j] = cells2[j]
                cl += str(cells2[j])
                
            if cl in seen:
                rep = i
                break
                break
            
            seen[cl] = True
        
        if rep == -1:
            return cells
        if n % rep == 0:
            n = rep
        else:
            n = n % rep
            
        cells = [c for c in cells_backup]
        
        for i in range(n):
            cells2 = [0] * 8
            for j in range(1, 7):
                cells2[j] = 1 - (cells[j - 1] ^ cells[j + 1])
            
            cells = [c for c in cells2] 
            
        return cells
