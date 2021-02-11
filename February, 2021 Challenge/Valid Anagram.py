class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cnt1 = [0] * 26
        cnt2 = [0] * 26
        
        for c in s:
            cnt1[ord(c) - ord('a')] += 1
        
        for c in t:
            cnt2[ord(c) - ord('a')] += 1
        
        for i in range(26):
            if cnt1[i] != cnt2[i]:
                return False
        
        return True
