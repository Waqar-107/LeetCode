class Solution:
    def toGoatLatin(self, S: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        words = S.split(" ");
        ans = []
        
        s = "a"
        for word in words:
            n = len(word)
                
            if word[0] in vowels:
                word += "ma"
            
            else:
                word = word[1:] + word[0] + "ma"
            
            ans.append(word + s)
            s += "a"
            
        return " ".join(ans)
            
            
