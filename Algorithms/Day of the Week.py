import datetime

class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        x = datetime.datetime(year, month, day)
        weekdays = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        
        return weekdays[int(x.strftime("%w"))]
