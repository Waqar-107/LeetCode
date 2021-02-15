class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        arr = []
        for i in range(len(mat)):
            arr.append((sum(mat[i]), i))
        
        arr.sort()
        
        ans = []
        for i in range(k):
            ans.append(arr[i][1])
        
        return ans
