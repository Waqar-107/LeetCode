class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        arr = set(words)
        
        for w in words:
            for i in range(1, len(w)):
                arr.discard(w[i:]);
        
        ans = 0
        arr = list(arr)
        for i in range(len(arr)):
            ans += len(arr[i])
        
        return ans + len(arr)
