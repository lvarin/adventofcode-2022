import re

stacks = {1: ['F','C','J','P','H','T','W'],
          2: ['G','R','V','F','Z','J','B','H'],
          3: ['H','P','T','R'],
          4: ['Z','S','N','P','H','T'],
          5: ['N','V','F','Z','H','J','C','D'],
          6: ['P','M','G','F','W','D','Z'],
          7: ['M','V','Z','W','S','J','D','P'],
          8: ['N','D','S'],
          9: ['D','Z','S','F','M'] 
         }

with open('input2') as file:
    for line in file:
        m = re.search('move (\d*) from (\d*) to (\d*)', line)
        times=int(m.group(1))
        origin=int(m.group(2))
        dest=int(m.group(3))

        for temp in stacks[origin][-times:]:
            stacks[dest].append(temp)

        for i in range(times):
            stacks[origin].pop()
        print("\n* %s" % line) 
        print(stacks)

for col in stacks:
    print(stacks[col][-1])
