with open('input') as file:
    line = file.readline()

    size=14

    for i in range(size,len(line)):
        marker=line[i-size:i]

        if(len(set(marker))==size):
            print("%d: %s" % (i,marker))
            break
