class Dust():
    pos=[0,500]

    def reset(self):
        self.pos=[0,500]

    def collisionD(self):
        try:
            return matrix[str([self.pos[0]+1,self.pos[1]])]>0
        except KeyError:
            return False

    def collisionL(self):
        try:
            return matrix[str([self.pos[0]+1,self.pos[1]-1])]>0
        except KeyError:
            return False

    def collisionR(self):
        try:
            return matrix[str([self.pos[0]+1,self.pos[1]+1])]>0
        except KeyError:
            return False

    def down(self):
        self.pos[0]+=1

    def down_left(self):
        self.pos[0]+=1
        self.pos[1]-=1

    def down_right(self):
        self.pos[0]+=1
        self.pos[1]+=1

    def __str__(self):
        return str(self.pos)

def fill(p1,p2):
    if p1[0]==p2[0]:
        start=min(p1[1],p2[1])
        end=max(p1[1],p2[1])
        for f in range(start,end+1):
            matrix[str([f,p1[0]])]=1
            # 1 is a wall
    else:
        start=min(p1[0],p2[0])
        end=max(p1[0],p2[0])
        for f in range(start,end+1):
            matrix[str([p1[1],f])]=1

matrix = {}

with open('input') as file:
    for line in file:
        line=line.replace('\n', ' ')
        point_words=[]
        for word in line.split(' '):
            if word == '->' or word =='':
                continue
            point_words.append(list(map(int,word.split(','))))
        for i in range(len(point_words)-1):
            fill(point_words[i],point_words[i+1])

total_dust=0

dust = Dust()

while dust.pos[0]<200:
    dust.reset()
    stop=False
    while not stop and dust.pos[0]<200:
        collitionD=False
        collitionL=False
        collitionR=False

        if not dust.collisionD():
            dust.down()
        elif not dust.collisionL():
            dust.down_left()
        elif not dust.collisionR():
            dust.down_right()
        else:
            matrix[str([dust.pos[0],dust.pos[1]])]=2  # 2 is a dust particle
            total_dust+=1
            stop=True                

print("Solution ",total_dust)

