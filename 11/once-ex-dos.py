import queue

class Monkey():
    items = []
    totalItems = 0
    divisible = 0
    op=None
     
    def enqueue(self, lista):

        self.items=lista
        
        #self.totalItems=len(self.items)
 
    def pop(self):
        return self.items.pop(0)

    def append(self, item):
        self.items.append(item)

    def inspect(self):
        self.totalItems=self.totalItems+1

m = []
turns=10000

m.append(Monkey())
m[0].divisible = 23
m[0].op = lambda old : old * 19
m[0].enqueue([79,98])
m[0].truem = 2
m[0].falsem = 3

m.append(Monkey())
m[1].divisible = 19
m[1].op = lambda old : old + 6
m[1].enqueue([54,65,75,74])
m[1].truem = 2
m[1].falsem = 0

m.append(Monkey())
m[2].divisible = 13
m[2].op = lambda old : old * old
m[2].enqueue([79,60,97])
m[2].truem = 1
m[2].falsem = 3

m.append(Monkey())
m[3].divisible = 17
m[3].op = lambda old : old + 3
m[3].enqueue([74])
m[3].truem = 0
m[3].falsem = 1

supermodule=1
for monk in m:
    supermodule *=monk.divisible

for turn in range(turns):
    for monkey in range(len(m)):
        while len(m[monkey].items):
            item = m[monkey].pop()
            item=m[monkey].op(item)
            m[monkey].inspect()
            item %=supermodule
            if item % m[monkey].divisible==0:
                m[m[monkey].truem].append(item)
            else:
                m[m[monkey].falsem].append(item)
    #print("---")
    #for monkey in range(len(m)):
    #    print(m[monkey].items)

for monkey in range(len(m)):
    print("Monkey %d inspected items %d times." % (monkey, m[monkey].totalItems))


