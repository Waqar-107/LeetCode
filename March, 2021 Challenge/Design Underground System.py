class UndergroundSystem:

    def __init__(self):
        self.pair_of_stations = {}
        self.check_in = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_in[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        otherStation = self.check_in[id][0]
        otherTime = self.check_in[id][1]
        
        if (otherStation, stationName) not in self.pair_of_stations:
            self.pair_of_stations[(otherStation, stationName)] = (0, 0)
        
        x = self.pair_of_stations[(otherStation, stationName)][0] + t - otherTime
        y = self.pair_of_stations[(otherStation, stationName)][1] + 1
        self.pair_of_stations[(otherStation, stationName)] = (x, y)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        if (startStation, endStation) in self.pair_of_stations:
            t = self.pair_of_stations[(startStation, endStation)][0]
            cnt = self.pair_of_stations[(startStation, endStation)][1]
            return t / cnt


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
