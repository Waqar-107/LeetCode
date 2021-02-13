class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        ans = 0
        q = len(sequence) // len(word)
        
        for k in range(1, q + 1):
            if sequence.find(word * k) != -1:
                ans = k
        
        return ans
