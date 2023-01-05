def getValue(i):
    return Xcycle[i-1]*i

def getXPos(i):
    return Xcycle[i]%40

X = 1
Xcycle = [1]

with open('input') as file:
    for line in file:
        line=line.replace('\n',' ')
        words = line.split(' ')

        Xcycle.append(X)

        if words[0]=='addx':
            X=X+int(words[1])
            Xcycle.append(X)

    #print(Xcycle)

i=0
for y in range(6):
    line="" 
    for x in range(40):
        if getXPos(i) in [x-1,x,x+1]:     
            pixel="#"
        else:
            pixel="."
        #print(getXPos(i),x,i,pixel)
        line=line+pixel
        i=i+1

    print(line)

