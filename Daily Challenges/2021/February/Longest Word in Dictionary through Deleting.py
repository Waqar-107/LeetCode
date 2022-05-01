class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        ans = ""
        n = len(s)
        
        for word in d:
            j = 0
            i = 0
            m = len(word)
            
            while j < n and i < m:
                if s[j] == word[i]:
                    i += 1
                    j += 1
                    
                else:
                    j += 1
            
            if i == m:
                if len(ans) < m:
                    ans = word
                
                elif len(ans) == m:
                    if ans > word:
                        ans = word
                
        return ans
            
