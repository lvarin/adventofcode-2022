def getPriority(letter):
    if(letter.isupper()):
        return ord(letter)-38
    return ord(letter)-96

suma=0
with open('input') as file:
    while True:
      team=[]
      for index in range(3):
          line=set(file.readline()[:-1])
          team.append(line)
      if(len(line)==0):
          break
      for letter in team[0].intersection(team[1]).intersection(team[2]):
          suma=suma+getPriority(letter)


print(suma)
