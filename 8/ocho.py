
grid = []

with open('input') as file:
    for line in file:
        grid.append(line.replace('\n',''))

visibles=0

xmax=len(grid)
for x in range(xmax):
    ymax=len(grid[x])
    for y in range(ymax):
        if x==0 or y==0 or x==len(grid)-1 or y==len(grid[x])-1:
            visibles=visibles+1
        else:
           
            visibleB=True
            for k in range(x+1,xmax):
                if grid[x][y]<=grid[k][y]:
                    visibleB=False
                    break

            visibleT=True
            for k in range(0,x):
                if grid[x][y]<=grid[k][y]:
                    visibleT=False
                    break
            
            visibleR=True
            for k in range(y+1,ymax):
                if grid[x][y]<=grid[x][k]:
                    visibleR=False
                    break

            visibleL=True
            for k in range(0,y):
                if grid[x][y]<=grid[x][k]:
                    visibleL=False
                    break
     
            if visibleB or visibleT or visibleR or visibleL:
                print("(%d,%d): %d" % (x,y,int(grid[x][y])))
                visibles=visibles+1


                

print(visibles)    
