class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        pat = [""] * 26
        arr = str.split(" ")
        
        n = len(pattern)
        if n != len(arr):
            return False
        
        for i in range(n):
            if pat[ord(pattern[i]) - ord('a')] == "":
                pat[ord(pattern[i]) - ord('a')] = arr[i]
            
            elif pat[ord(pattern[i]) - ord('a')] != arr[i]:
                return False
        
        t1 = set()
        for i in range(26):
            if pat[i] != "":
                t1.add(pat[i])
                
        t2 = set()
        for i in range(n):
            t2.add(pattern[i])
        
        return len(t1) == len(t2)
        
