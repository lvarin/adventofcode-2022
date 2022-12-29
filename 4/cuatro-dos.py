count=0

with open('input') as file:
    for line in file:
        line = line.replace('\n', '')
        lineSplit = line.split(',')
        uno=lineSplit[0].split('-')
        dos=lineSplit[1].split('-')

        if(int(uno[0])>int(dos[1]) or int(uno[1])<int(dos[0])):
            print(line)
        else:
            count=count+1

print(count)
