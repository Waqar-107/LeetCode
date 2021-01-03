class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        s = set()
        for w in words:
            x = ""
            for i in range(len(w)):
                x += morse[ord(w[i]) - ord('a')]
            
            s.add(x)
        
        return len(s)
