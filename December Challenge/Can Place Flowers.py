class Solution:
    def canPlaceFlowers(self, flowers: List[int], n: int) -> bool:
        if len(flowers) == 1:
            cnt = 0
            if flowers[0] == 0:
                cnt += 1
            
            return cnt >= n
        
        cnt = 0
        for i in range(len(flowers)):
            if flowers[i] == 0:
                if i == 0:
                    if i + 1 < len(flowers) and flowers[i + 1] == 0:
                        cnt += 1
                        flowers[i] = 1
                        
                elif i != len(flowers) - 1:
                    if flowers[i - 1] == 0 and i + 1 < len(flowers) and flowers[i + 1] == 0:
                        cnt += 1
                        flowers[i] = 1
                
                else:
                    if i - 1 >= 0 and flowers[i - 1] == 0:
                        cnt += 1
                        flowers[i] = 1
                
                # print(flowers)
        
        return cnt >= n
