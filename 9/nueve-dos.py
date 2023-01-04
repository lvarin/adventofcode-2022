def distance(H,T):
    return max(abs(H[0]-T[0]),abs(H[1]-T[1]))

def isDiagonal(H,T):
    return abs(H[0]-T[0])>0 and abs(H[1]-T[1])>0

def move(direction, H):
    if direction=='R':
            H[1]=H[1]+1
    elif direction=='L':
            H[1]=H[1]-1
    elif direction=='U':
            H[0]=H[0]+1
    elif direction=='D':
            H[0]=H[0]-1
    
    return H

def moveD(H,T):
    if H[0]>T[0]:
        T[0]=T[0]+1
    elif H[0]<T[0]:
        T[0]=T[0]-1

    if H[1]>T[1]:
        T[1]=T[1]+1
    elif H[1]<T[1]:
        T[1]=T[1]-1

    return T

def whatDirection(H,T):
    if H[1]>T[1]:
        return 'R'
    if H[1]<T[1]:
        return 'L'
    if H[0]>T[0]:
        return 'U'
    if H[0]<T[0]:
        return 'D'

def printMatrix(positions):
    for i in range(15,-6,-1):
        line="%02d " % i
        for j in range(-11,17):
            if [0,0] == [i,j]:
                line=line+"s"
            elif {"[%d, %d]" % (i,j)}.issubset(positions):
                line=line+"#"
            else:
                line=line+"."
        print(line)

s=[0,0]
H=[[0,0],
   [0,0],
   [0,0],
   [0,0],
   [0,0],
   [0,0],
   [0,0],
   [0,0],
   [0,0],
   [0,0]]

print(H)

positions = set()
positions.add(str(H[9]))

with open('input') as file:
    for line in file:
        line=line.replace('\n',' ')
        words=line.split(' ')

        direction = words[0]
        times = int(words[1])

        for i in range(times):
            H[0]=move(direction,H[0])

            for i in range(1,10):            
                distanceHT = distance(H[i-1],H[i])

                if distanceHT>1:
                    if not isDiagonal(H[i-1],H[i]):
                        H[i]=move(whatDirection(H[i-1],H[i]),H[i])
                    else:
                        H[i]=moveD(H[i-1],H[i])

            positions.add(str(H[9]))
            print("[%s %d] %s" % (direction, times, H))        

#print(s,T,H)
printMatrix(positions)

print(len(positions))
