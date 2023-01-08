'''
   Following: https://en.wikipedia.org/wiki/Breadth-first_search
'''

def edges(p):
    '''
        returns the point accesible tpo the one given as parameter
    '''
    edgesList=[]

    possibles=[
               [p[0]-1,p[1]],
               [p[0]+1,p[1]],
               [p[0],  p[1]-1],
               [p[0],  p[1]+1]
              ]

    for pos in possibles:
        if pos[0]>=0 and pos[1]>=0 and isAccesible(p,pos):
            edgesList.append(pos)

    #print("EdgesList: %s" % edgesList)
    return edgesList

def isAccesible(p,pdos):
    '''
       are these two points accesible one tp the other
    '''

    p_val=matrix[p[0]][p[1]]
    try:
        pdos_val=matrix[pdos[0]][pdos[1]]
    except IndexError:
        return False

    return pdos_val+1>=p_val

def printParents(n,solution,parents):
    '''
       returns the list of parents of a given points, recursively
    '''
    try:
        parent=parents[str(n)]
    except KeyError:
        if solution==0:
            return float('inf')
        return solution
    #print(parent)
    return printParents(parent,solution+1,parents)

parents = {}

def BFS(S):
    Q=[]
    explored=[]
    explored.append(E)
    Q.append(E)

    while Q:
        #print(Q)
        v = Q.pop(0)
        if v == S:
            break
        for w in edges(v):
            if w not in explored:
                explored.append(w)
                #print("Parent of %s is %s" % (w,v))
                try:
                    parents[str(w)]
                except KeyError:
                    parents[str(w)]=v
                    Q.append(w)
    #print("end")
    return printParents(S,0,parents)

E=[-1,-1]

minus=ord('a')

matrix = []

startingPoints = []

with open('input') as file:
    x=0
    for line in file:
        matrixLine=[]
        line=line.replace('\n','')
        y=0
        for letter in line:
            if letter=='S':
                letter='a'
                startingPoints.append([x,y])
            elif letter=='E':
                letter='z'
                E=[x,y]
            elif letter=='a':
                startingPoints.append([x,y])
            matrixLine.append(int(ord(letter)-minus))
            y +=1
        matrix.append(matrixLine)
        x +=1

solutions = []

i=0
for Start in startingPoints:
    i +=1
    solutions.append(BFS(Start))

print(min(solutions))
