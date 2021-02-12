class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        arr = []
        for i in range(1, n + 1):
            arr.append(i)
            
        arr.sort(key=lambda x : str(x))
        return arr
