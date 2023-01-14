import re

class Sensor():
    sensor=[]
    beacon=[]
    distance=0

    def __init__(self,sensor,beacon):
        self.sensor=list(map(int,sensor))
        self.beacon=list(map(int,beacon))
        self.distance=getDistance(self.sensor,self.beacon)
        print("New sensor distance: ",self.distance)

    def __str__(self):
        return "%s -> %s" % (self.sensor, self.beacon)

    def inArea(self,point):
        return getDistance(self.sensor,point)<=self.distance

    def getXLimit(self,y):
        Z=self.distance-abs(self.sensor[1]-y)
        return [self.sensor[0]-Z, self.sensor[0]+Z]

def getDistance(p1, p2):
    return abs(p1[0]-p2[0])+abs(p1[1]-p2[1])

sensors=[]

with open('input') as file:
    for line in file:
        line=line.replace('\n','')
        numbers=re.match(r'Sensor at x=(-?\d*), y=(-?\d*): closest beacon is at x=(-?\d*), y=(-?\d*)',line)
        s=Sensor(numbers.groups()[0:2], numbers.groups()[2:4])
        sensors.append(s)

start=0
limit = 4000000

multiplier=4000000

x=0
y=0
oldsol=[x,y]
while y<=limit and x<=limit:
    for sen in sensors:
        if sen.inArea([x,y]):
            x=sen.getXLimit(y)[1]+1
            if x>limit:
                y+=1
                x=0
    if oldsol==[x,y]:
        print("x=%d, y=%d, solution=%d" % (x,y,x*multiplier+y))
        break
    oldsol=[x,y]
    print("Current search:",y,x)
