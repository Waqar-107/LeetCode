class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        ret = []
        for i in A:
            if i % 2 == 0:
                ret.append(i)
        
        for i in A:
            if i % 2:
                ret.append(i)
        
        return ret
        
