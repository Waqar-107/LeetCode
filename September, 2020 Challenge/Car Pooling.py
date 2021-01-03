import heapq

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        tripList = []
        n = len(trips)
        
        for i in range(n):
            tripList.append((trips[i][0], trips[i][1], trips[i][2]))
        
        # sorting according to starting time
        tripList.sort(key = lambda x: (x[1]))
        
        tripQ = []
         
        for i in range(n):
            # free heap
            while len(tripQ):
                en, total, st = min(tripQ)
                if en <= tripList[i][1]:
                    heapq.heappop(tripQ)
                    capacity += total
                else:
                    break
            
            if capacity >= tripList[i][0]:
                capacity -= tripList[i][0]
                heapq.heappush(tripQ, (tripList[i][2], tripList[i][0], tripList[i][1]))
            
            else:
                return False
        
        return True
        
        
