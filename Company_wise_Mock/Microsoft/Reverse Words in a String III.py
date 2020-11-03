class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        ans = []
        
        for word in words:
            ans.append(word[::-1])
        
        return " ".join(ans)
