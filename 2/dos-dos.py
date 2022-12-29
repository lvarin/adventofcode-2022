with open('input') as file:
    lines = file.readlines()

score=0
for l in lines:
   they=l[0]
   you=l[2]
   
   if(you=='X'):
       score+=1
       if(they=='A'):
           score=score+3
       elif(they=='B'):
           score=score+0
       elif(they=='C'):
           score=score+6
   elif(you=='Y'):
       score=score+2
       if(they=='A'):
           score=score+6
       elif(they=='B'):
           score=score+3
       elif(they=='C'):
           score=score+0
   elif(you=='Z'):
       score=score+3
       if(they=='A'):
           score=score+0
       elif(they=='B'):
           score=score+6
       elif(they=='C'):
           score=score+3
 
print(score)
