from itertools import permutations

class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        perm = permutations(str(N)) 
        
        for lst in list(perm): 
            num = "".join(lst)
            
            if num[0] == '0':
                continue
            
            if bin(int(num)).count('1') == 1:
                return True
        
        return False;
