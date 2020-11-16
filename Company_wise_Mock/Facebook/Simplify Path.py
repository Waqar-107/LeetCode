class Solution:
    def simplifyPath(self, path: str) -> str:
        folders = path.split("/")
        
        stk = []
        for f in folders:
            if f == "" or f == ".":
                continue
            
            if f == ".." and len(stk):
                stk.pop()
            
            elif f != "..":
                stk.append(f)
        
        return "/" + "/".join(stk)
