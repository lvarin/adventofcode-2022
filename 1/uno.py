
with open('input') as file:
    lines = file.readlines()

sum=0
max=0
for l in lines:
    try:
      sum=sum+int(l)
    except ValueError:
      if (max<sum):
          max=sum
      sum=0

print(max)
