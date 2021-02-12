class TrieNode:
    def __init__(self):
        self.sum = 0
        self.alpha = [None] * 26

class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, s, val):
        root = self.root
        for i in range(len(s)):
            id = ord(s[i]) - ord('a')
            if not root.alpha[id]:
                root.alpha[id] = TrieNode()
            
            root.alpha[id].sum += val
            root = root.alpha[id]
    
    def subtract(self, s, val):
        root = self.root
        for i in range(len(s)):
            id = ord(s[i]) - ord('a')
            
            root.alpha[id].sum -= val
            root = root.alpha[id]
    
    def getPrefixSum(self, s):
        root = self.root
        for i in range(len(s)):
            id = ord(s[i]) - ord('a')
            
            if root.alpha[id] == None:
                return 0
            
            if i == len(s) - 1:
                return root.alpha[id].sum
            
            root = root.alpha[id]
        
        return 0
        

class MapSum:

    def __init__(self):
        self.trie = Trie()
        self.dict = {}

    def insert(self, key: str, val: int) -> None:
        if key in self.dict:
            self.trie.subtract(key, self.dict[key])
        
        self.trie.insert(key, val)
        self.dict[key] = val

    def sum(self, prefix: str) -> int:
        return self.trie.getPrefixSum(prefix)
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
