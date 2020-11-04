class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = list(map(int, version1.split(".")))
        v2 = list(map(int, version2.split(".")))
        
        while len(v1) > len(v2):
            v2.append(0)
        
        while len(v2) > len(v1):
            v1.append(0)
        
        if v1 < v2:
            return -1
        elif v1 > v2:
            return 1
        
        return 0
