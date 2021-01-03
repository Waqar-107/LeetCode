class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if duration == 0 or len(timeSeries) == 0:
            return 0
        
        oldL = timeSeries[0]
        oldR = timeSeries[0] + duration - 1
        
        arr = []
        arr.append([oldL, oldR])
        
        k = 0
        for i in range(1, len(timeSeries), 1):
            if timeSeries[i] > arr[k][1]:
                arr.append([timeSeries[i], timeSeries[i] + duration - 1])
                k += 1
            else:
                arr[k][1] = timeSeries[i] + duration - 1
        
        ans = 0
        for i in range(len(arr)):
            ans += arr[i][1] - arr[i][0] + 1
        
        return ans
