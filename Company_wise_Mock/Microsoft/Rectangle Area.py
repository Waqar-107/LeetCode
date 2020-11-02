class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        area1 = abs(A - C) * abs(B - D)
        area2 = abs(E - G) * abs(F - H)
        
        arrX = [A, C, E, G]
        arrY = [B, D, F, H]
        
        arrX.sort()
        arrY.sort()
        
        print(arrX, arrY)
        
        # one is on the right to the other
        if G <= A or C <= E:
            intersectedArea = 0
        # one is above another
        elif D <= F or H <= B:
            intersectedArea = 0
        else:
            intersectedArea = abs(arrX[1] - arrX[2]) * abs(arrY[1] - arrY[2])
        print(area1, area2, intersectedArea)
        return area1 + area2 - intersectedArea
