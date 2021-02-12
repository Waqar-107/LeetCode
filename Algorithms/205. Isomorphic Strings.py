class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        char_mapping_s = {}
        char_mapping_t = {}
        
        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            if s[i] in char_mapping_s:
                if t[i] != char_mapping_s[s[i]]:
                    return False
            
            else:
                if t[i] in char_mapping_t:
                    return False
                
                char_mapping_s[s[i]] = t[i]
                char_mapping_t[t[i]] = s[i]
        
        return True
