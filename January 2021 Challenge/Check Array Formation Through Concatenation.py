class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        n = len(arr)
        for p in pieces:
            for i in range(n):
                if p[0] == arr[i]:
                    for j in range(len(p)):
                        if i + j >= n or p[j] != arr[i + j]:
                            return False
                        else:
                            arr[i + j] = 0
                    
                    break
        
        if sum(arr) != 0:
            return False
        
        return True
