class Solution:
    def __init__(self):
        self.dp = {}
        self.dictionary = {}
    
    def solve(self, s):
        n = len(s)
        
        if n == 0:
            return True
        
        if s in self.dp:
            return self.dp[s]
        
        # check all possible substrings that are in the dictionary
        # if a substr is in dictionary then check the rest
        for i in range(n):
            sub = s[: (i + 1)]
            if sub in self.dictionary:
                if self.solve(s[i + 1 :]):
                    self.dp[s] = True
                    return self.dp[s]
        
        self.dp[s] = False
        return self.dp[s]
                    
    
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        for d in wordDict:
            self.dictionary[d] = True
        
        return self.solve(s)
        
