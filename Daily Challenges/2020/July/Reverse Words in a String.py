class Solution:
    def reverseWords(self, s: str) -> str:
        arr = s.split(' ')
        ans = []
        
        for word in arr:
            if len(word):
                ans.append(word)
        
        ans = ans[::-1]
        return " ".join(ans)
