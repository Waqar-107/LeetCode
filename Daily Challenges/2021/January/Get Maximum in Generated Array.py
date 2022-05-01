class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        arr = [0] * (101)
        arr[1] = 1
        
        for i in range(2, n + 1):
            if i % 2 == 0:
                arr[i] = arr[i // 2]
            else:
                arr[i] = arr[i // 2] + arr[i // 2 + 1]
        
        return max(arr[:n + 1])
            
