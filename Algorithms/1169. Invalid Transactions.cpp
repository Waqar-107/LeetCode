from collections import deque

class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        
        ans = set()
        names = {}
        n = len(transactions)
        for i in range(n):
            t = transactions[i]
            
            arr = t.split(',')
            if arr[0] not in names:
                names[arr[0]] = []
            
            
            tup = (int(arr[1]), int(arr[2]), arr[3], i)
            names[arr[0]].append(tup)
            
            if int(arr[2]) > 1000:
                ans.add(t)
        
        for nam in names:
            # sort using time
            names[nam].sort(key=lambda x: x[0])
            
            l = 0
            r = 0
            n = len(names[nam])
            city = set()
            city_map = {}
            idx = deque()
            
            while r < n:
                if names[nam][r][0] - names[nam][l][0] <= 60:
                    city.add(names[nam][r][2])
                    
                    # the index of the actual string
                    idx.append(names[nam][r][3])
                    
                    if names[nam][r][2] not in city_map:
                        city_map[names[nam][r][2]] = 0
                        
                    city_map[names[nam][r][2]] += 1 
                    
                    r += 1
                    
                else:
                    break
           
            nxt_start = 0
            if len(city) > 1:
                for i in idx:
                    ans.add(transactions[i])
                
                nxt_start = len(idx)
                
            # making a sliding window
            while l < n and r < n:
                while names[nam][r][0] - names[nam][l][0] > 60:
                    city_map[names[nam][l][2]] -= 1
                    
                    if city_map[names[nam][l][2]] == 0:
                        city.remove(names[nam][l][2])
                    
                    l += 1
                
                
                nxt_start = max(nxt_start, l)
                
                # now take r in the window, from l-r all of them are invalid if city > 1
                if names[nam][r][2] not in city_map:
                    city_map[names[nam][r][2]] = 0
                    
                city_map[names[nam][r][2]] += 1
                city.add(names[nam][r][2])
                idx.append(names[nam][r][3])
               
                # now either l == r or l < r
                if len(city) > 1:
                    for j in range(nxt_start, len(idx), 1):
                        ans.add(transactions[idx[j]])
                    
                    nxt_start = len(idx)
                
                r += 1

        return ans 

# this problem was a nightmare
