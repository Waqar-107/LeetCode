class Solution:
    def customSortString(self, S: str, T: str) -> str:
        rank = defaultdict(int)
        
        for i in range(len(S)):
            rank[S[i]] = i + 1
        
        arr = []
        for i in range(len(T)):
            arr.append(T[i])
            if T[i] not in rank:
                rank[T[i]] = len(S) + 1
        
        arr.sort(key = lambda x : (rank[x]))
        return "".join(arr)