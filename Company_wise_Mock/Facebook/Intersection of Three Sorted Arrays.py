class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        ans = []
        n = len(arr1)
        
        for i in range(n):
            x = bisect.bisect_right(arr2, arr1[i], 0, n)
            y = bisect.bisect_right(arr3, arr1[i], 0, n)
            
            if arr2[x - 1] == arr1[i] and arr3[y - 1] == arr1[i]:
                ans.append(arr1[i])
                
        return ans
