class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        n = len(popped)
        vis = {}
        p = 0
        stack = []
        
        for i in range(n):
            if popped[i] in vis:
                if stack[-1] == popped[i]:
                    stack.pop()
                else:
                    return False
            
            else:
                while p < n:
                    vis[pushed[p]] = True

                    if popped[i] == pushed[p]:
                        p += 1
                        break
                    else:
                        stack.append(pushed[p])
                        p += 1
                
        return True
