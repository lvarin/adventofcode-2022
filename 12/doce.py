#
# https://en.wikipedia.org/wiki/Breadth-first_search
#

def edges(p):
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
    p_val=matrix[p[0]][p[1]]
    try:
        pdos_val=matrix[pdos[0]][pdos[1]]
    except IndexError:
        return False
    
    return pdos_val+1>=p_val

def printParents(n,solution):
    try:
        parent=parents[str(n)]
    except KeyError:
        return solution
    print(parent)
    return printParents(parent,solution+1)

S=[-1,-1]
E=[-1,-1]

minus=ord('a')

matrix = []

with open('input') as file:
    x=0
    for line in file:
        matrixLine=[]
        line=line.replace('\n','')
        y=0
        for letter in line:
            if letter=='S':
                letter='a'
                S=[x,y]
            elif letter=='E':
                letter='z'
                E=[x,y]
            matrixLine.append(int(ord(letter)-minus))
            y +=1
        matrix.append(matrixLine)
        x +=1

print("S: %s" % S)
print("E: %s" % E)

print(matrix)
print('---')

Q=[]
explored=[]
explored.append(E)
Q.append(E)

parents = {}

while len(Q):
    #print(Q)
    v = Q.pop(0)
    if v == S:
        print("Arrived! to %s" % S)
        break
    for w in edges(v):
        if w not in explored:
            explored.append(w)
            print("Parent of %s is %s" % (w,v))
            parents[str(w)]=v
            Q.append(w)
print("end")

solution =printParents(S,0)

print("Solution: %d" % solution)

