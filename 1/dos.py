
with open('input') as file:
    lines = file.readlines()

suma=0
sums=[]
for l in lines:
    try:
      suma=suma+int(l)
    except ValueError:
      sums.append(suma)
      suma=0

print(sum(sorted(sums,reverse=True)[0:3]))
