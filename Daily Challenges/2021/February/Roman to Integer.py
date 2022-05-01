class Solution:
    def romanToInt(self, s: str) -> int:
        roman_decimal_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        i = 0
        n = len(s)
        ans = 0
        
        while i < n:
            if s[i] == 'I' and i + 1 < n and (s[i + 1] == 'V' or s[i + 1] == 'X'):
                if s[i + 1] == 'V':
                    ans += 4
                else:
                    ans += 9
                
                i += 2
            
            elif s[i] == 'X' and i + 1 < n and (s[i + 1] == 'L' or s[i + 1] == 'C'):
                if s[i + 1] == 'L':
                    ans += 40
                else:
                    ans += 90
                
                i += 2
            
            elif s[i] == 'C' and i + 1 < n and (s[i + 1] == 'D' or s[i + 1] == 'M'):
                if s[i + 1] == 'D':
                    ans += 400
                else:
                    ans += 900
                
                i += 2
            
            else:
                ans += roman_decimal_map[s[i]]
                i += 1
        
        return ans
