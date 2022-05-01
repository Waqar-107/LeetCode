class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        s = s.lower()
        uno, dos = 0, 0
        
        n = len(s)
        vowel = ['a', 'e', 'i', 'o', 'u']
        
        for i in range(n // 2):
            if s[i] in vowel:
                uno += 1
        
        for i in range(n // 2, n):
            if s[i] in vowel:
                dos += 1
        
        return uno == dos
