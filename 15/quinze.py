import re

class Sensor():
    sensor=[]
    beacon=[]

    def __init__(self,sensor,beacon):
        self.sensor=list(map(int,sensor))
        self.beacon=list(map(int,beacon))

    def __str__(self):
        return "%s -> %s" % (self.sensor, self.beacon)

    def inArea(self,point):
        return distance(self.sensor,point)<=distance(self.sensor,self.beacon)

def distance(p1, p2):
    return abs(p1[0]-p2[0])+abs(p1[1]-p2[1])

def getLimits(sensors,y):
    minimumX=0
    maximumX=0

    for sensor in sensors:
        dist=distance(sensor.sensor, sensor.beacon)
        minimumX=min(sensor.sensor[0]-dist, minimumX)
        maximumX=max(sensor.sensor[0]+dist, maximumX)
    return [minimumX, maximumX]

sensors=[]
beacons=[]

with open('input') as file:
    for line in file:
        line=line.replace('\n','')
        numbers=re.match(r'Sensor at x=(-?\d*), y=(-?\d*): closest beacon is at x=(-?\d*), y=(-?\d*)',line)
        s=Sensor(numbers.groups()[0:2], numbers.groups()[2:4])
        sensors.append(s)
        beacons.append(s.beacon)
y=2000000

limits=getLimits(sensors,y)

hits = {}

for x in range(limits[0],limits[1]+1):
    for sensor in sensors:
        if sensor.inArea([x,y]) and not [x,y] in beacons:
            hits[str([x,y])]=True
            break

print("Solution: ",len(hits))
