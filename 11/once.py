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
turns=20

m.append(Monkey())
m[0].divisible = 2
m[0].op = lambda old : old * 17
m[0].enqueue([85,79,63,72])
m[0].truem = 2
m[0].falsem = 6

m.append(Monkey())
m[1].divisible = 7
m[1].op = lambda old : old * old
m[1].enqueue([53,94,65,81,93,73,57,92])
m[1].truem = 0
m[1].falsem = 2

m.append(Monkey())
m[2].divisible = 13
m[2].op = lambda old : old + 7 
m[2].enqueue([62,63])
m[2].truem = 7
m[2].falsem = 6

m.append(Monkey())
m[3].divisible = 5
m[3].op = lambda old : old + 4
m[3].enqueue([57,92,56])
m[3].truem = 4
m[3].falsem = 5

m.append(Monkey())
m[4].divisible = 3
m[4].op = lambda old : old + 5
m[4].enqueue([67])
m[4].truem = 1
m[4].falsem = 5

m.append(Monkey())
m[5].divisible = 19
m[5].op = lambda old : old + 6
m[5].enqueue([85,56,66,72,57,99])
m[5].truem = 1
m[5].falsem = 0

m.append(Monkey())
m[6].divisible = 11
m[6].op = lambda old : old * 13
m[6].enqueue([86,65,98,97,69])
m[6].truem = 3
m[6].falsem = 7

m.append(Monkey())
m[7].divisible = 17
m[7].op = lambda old : old + 2
m[7].enqueue([87,68,92,66,91,50,68])
m[7].truem = 4
m[7].falsem = 3

for turn in range(turns):
    for monkey in range(len(m)):
        while len(m[monkey].items):
            item = m[monkey].pop()
            item=int(m[monkey].op(item)/3)
            m[monkey].inspect()
            if item % m[monkey].divisible==0:
                m[m[monkey].truem].append(item)
            else:
                m[m[monkey].falsem].append(item)
    print("---")
    for monkey in range(len(m)):
        print(m[monkey].items)

for monkey in range(len(m)):
    print("Monkey %d inspected items %d times." % (monkey, m[monkey].totalItems))


