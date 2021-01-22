class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
     
        cnt1 = [0] * 26
        cnt2 = [0] * 26
        
        presence1 = [0] * 26
        presence2 = [0] * 26
        
        for c in word1:
            cnt1[ord(c) - ord('a')] += 1
            presence1[ord(c) - ord('a')] = 1
        
        for c in word2:
            cnt2[ord(c) - ord('a')] += 1
            presence2[ord(c) - ord('a')] = 1
            
        cnt1.sort()
        cnt2.sort()
            
        return cnt1 == cnt2 and presence1 == presence2
        
