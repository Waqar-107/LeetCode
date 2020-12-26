class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], x[1]))

        currently_available = 0
        total_needed = 0
        meetings = []

        for i in range(len(intervals)):
            while len(meetings):
                end_time = heapq.heappop(meetings)

                # this task is not done yet, put it in the heap again
                if end_time > intervals[i][0]:
                    heapq.heappush(meetings, end_time)
                    break
                # else the meeting is over by now so free a meeting room
                else:
                    currently_available += 1

            if currently_available > 0:
                currently_available -= 1
            else:
                total_needed += 1

            heapq.heappush(meetings, intervals[i][1])

        return total_needed
