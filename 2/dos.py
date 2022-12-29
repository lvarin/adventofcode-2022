with open('input') as file:
    lines = file.readlines()

score=0
for l in lines:
   they=l[0]
   you=l[2]
   
   if(you=='X'):
       score+=0
       if(they=='A'): # lose
           score=score+3
       elif(they=='B'):
           score=score+1
       elif(they=='C'):
           score=score+2
   elif(you=='Y'): # draw
       score=score+3
       if(they=='A'):
           score=score+1
       elif(they=='B'):
           score=score+2
       elif(they=='C'):
           score=score+3
   elif(you=='Z'): # win
       score=score+6
       if(they=='A'):
           score=score+2
       elif(they=='B'):
           score=score+3
       elif(they=='C'):
           score=score+1
 
print(score)
