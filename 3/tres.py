def getPriority(letter):
    if(letter.isupper()):
        return ord(letter)-38
    return ord(letter)-96

with open('input') as file:
    lines = file.readlines()

suma=0
for line in lines:
    middle = int(len(line)/2)
    for letter in set(line[:middle]).intersection(set(line[middle:])):
        suma=suma+getPriority(letter)

print(suma)
