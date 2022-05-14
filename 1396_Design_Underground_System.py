class UndergroundSystem:

    def __init__(self):
        self.train={}
        self.distance = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.train[id]=(stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        st_name, t1 = self.train.get(id)
        time = t-t1
        # print(t,t1,st_name)
        map_str=st_name+'#'+stationName
        map_str1= stationName+'#'+st_name
        if self.distance.get(map_str) is None:
            self.distance[map_str] = list()
        self.distance[map_str].append(time)
        # print(self.distance)
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        map_str= startStation+'#'+endStation
        total = 0
        for t in self.distance[map_str]:
            total+=t
        cnt = len(self.distance[map_str])
        average = float(total)/cnt
        # print('average',average)
        return average


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)