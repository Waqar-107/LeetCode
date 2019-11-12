# from dust i have come, dust i will be

class Solution:
    def toGoatLatin(self, S: str) -> str:
        arr = S.split(' ')
        
        ret = ''
        k = 1
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        
        n = len(arr)
        for i in range(n):
            if arr[i][0] in vowels:
                s = arr[i] + 'ma' + ('a' * k)
            else:
                s = arr[i][1:] + arr[i][0] + 'ma' + ('a' * k)
            
            ret += s
            if i != n - 1:
                ret += ' '
            
            k += 1
        
        return ret
