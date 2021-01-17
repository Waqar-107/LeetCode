class Solution:
    @functools.lru_cache(None)
    def solve(self, vowel_no, length_rem):
        if vowel_no == 6:
            return 0
        
        if length_rem == 0:
            return 1
        
        return self.solve(vowel_no + 1, length_rem) + self.solve(vowel_no, length_rem - 1) 
        
            
    def countVowelStrings(self, n: int) -> int:
        return self.solve(1, n)
