class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        n = len(s)
        
        cnt1 = [0] * 26
        cnt2 = [0] * 26
        
        for i in range(n):
            cnt1[ord(s[i]) - ord('a')] += 1
            cnt2[ord(t[i]) - ord('a')] += 1
        
        cnt2[ord(t[n]) - ord('a')] += 1
        
        for i in range(26):
            if cnt1[i] + 1 == cnt2[i]:
                return chr(i + 97)
        
