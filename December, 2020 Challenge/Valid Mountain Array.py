class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        idx = -1
        for i in range(1, len(arr) - 1):
            if arr[i - 1] < arr[i] and arr[i] > arr[i + 1]:
                idx = i
                break
        
        if idx == -1:
            return False
        
        for i in range(idx, len(arr) - 1):
            if arr[i] > arr[i + 1]:
                continue
            
            return False
        
        for i in range(idx):
            if arr[i] < arr[i + 1]:
                continue
            
            return False
        
        return True
