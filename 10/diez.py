def getValue(i):
    return Xcycle[i-1]*i

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

        else:
            print(words[0])

    print(Xcycle)

    sum = getValue(20)+getValue(60)+getValue(100)+getValue(140)+getValue(180)+getValue(220)

    print("20th: %d, 60th: %d, 100th: %d, 140th: %d, 180th: %d, 220th: %d. Sum: %d" % (getValue(20), getValue(60), getValue(100), getValue(140), getValue(180), getValue(220), sum))
