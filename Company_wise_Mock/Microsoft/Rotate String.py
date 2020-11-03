class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False
        
        n = len(A)
        if n == 0:
            return True
        
        for i in range(n):
            A = A[1:] + A[0]
            if A == B:
                return True
        
        return False
