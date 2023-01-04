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
    if H[0]<T[0]:
        T[0]=T[0]-1

    if H[1]>T[1]:
        T[1]=T[1]+1
    if H[1]<T[1]:
        T[1]=T[1]-1

    return T

s=[0,0]
H=[0,0]
T=[0,0]

positions = set()
positions.add(str(T))

with open('input') as file:
    for line in file:
        line=line.replace('\n',' ')
        words=line.split(' ')

        direction = words[0]
        times = int(words[1])

        for i in range(times):
            H=move(direction,H)
            distanceHT = distance(H,T)

            if distanceHT>1:
                if not isDiagonal(H,T):
                    T=move(direction,T)
                else:
                    T=moveD(H,T)

            positions.add(str(T))
            print("[%s] T: %s, H: %s (%d)" % (direction,T,H, distanceHT))        

print(s,T,H)
print(positions)

print(len(positions))
