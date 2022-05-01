class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = list(map(int, version1.split(".")))
        v2 = list(map(int, version2.split(".")))
        
        n = max(len(v1), len(v2))
        
        for i in range(len(v1), n, 1):
            v1.append(0)
        for i in range(len(v2), n, 1):
            v2.append(0)
        
        for i in range(n):
            if v1[i] > v2[i]:
                return 1
            elif v1[i] < v2[i]:
                return -1
        
        return 0
        
