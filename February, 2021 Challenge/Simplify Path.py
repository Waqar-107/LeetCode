class Solution:
    def simplifyPath(self, path: str) -> str:
        new_path = ""
        n = len(path)
        
        i = 0
        while i < n:
            if path[i] == '/':
                new_path += '/'
                
                i + 1
                while i < n and path[i] == '/':
                    i += 1
            else:
                new_path += path[i]
                i += 1
            
        stack = []
        arr = new_path.split('/')
        
        for i in range(len(arr)):
            if len(arr[i]) == 0 or arr[i] == '.':
                continue
            
            if arr[i] == '..':
                if len(stack):
                    stack.pop()
            
            else:
                stack.append(arr[i])
            
        return "/" + "/".join(stack)
                    
