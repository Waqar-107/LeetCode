class Solution:
    def convert(self, word):
        vowels = ['a', 'e', 'i', 'o', 'u']
        temp = []
        for ch in word:
            if ch in vowels:
                temp.append("*")
            else:
                temp.append(ch)
        
        return "".join(temp)
    
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        cap = {}
        vowel = {}
        direct = {}
        
        for word in wordlist:
            direct[word] = True
            
            temp = word.lower()
            if temp not in cap:
                cap[temp] = word
            
            temp = self.convert(word.lower())
            if temp not in vowel:
                vowel[temp] = word
        
        ans = []
        
        for word in queries:
            if word in direct:
                ans.append(word)
                
            elif word.lower() in cap:
                ans.append(cap[word.lower()])
            else:
                temp = self.convert(word.lower())
                if temp in vowel:
                    ans.append(vowel[temp])
                else:
                    ans.append("")
        
        return ans
            
