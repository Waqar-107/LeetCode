class Solution:   
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        l = len(endWord)
        adj = defaultdict(list)
        dist = defaultdict(int)
        vis = {}
        
        for word in wordList:
            for i in range(l):
                adj[word[:i] + "*" + word[i + 1:]].append(word)
        
        q = [beginWord]
        vis[beginWord] = True
        dist[beginWord] = 1
        
        while len(q):
            u = q.pop(0)
            lvl = dist[u]
            
            for i in range(l):
                temp = u[:i] + "*" + u[i + 1:]
                for word in adj[temp]:
                    if word == endWord:
                        return lvl + 1
                    if word not in vis:
                        vis[word] = True
                        q.append(word)
                        dist[word] = lvl + 1
                adj[temp] = []
        
        return 0
        
        
        
