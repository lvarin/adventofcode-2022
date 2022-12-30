
grid = []

with open('input') as file:
    for line in file:
        grid.append(line.replace('\n',''))

visibles=0

xmax=len(grid)

maxiv=0

for x in range(1,xmax-1):
    ymax=len(grid[x])
    for y in range(1,ymax-1):

        visibleB=0
        for k in range(x+1,xmax):
            visibleB=visibleB+1
            if grid[x][y]<=grid[k][y]:
                break

        visibleT=0
        for k in range(x-1,-1,-1):
            visibleT=visibleT+1
            if grid[x][y]<=grid[k][y]:
                break

        visibleR=0
        for k in range(y+1,ymax):
            visibleR=visibleR+1
            if grid[x][y]<=grid[x][k]:
                break

        visibleL=0
        for k in range(y-1,-1,-1):
            visibleL=visibleL+1
            if grid[x][y]<=grid[x][k]:
                break

        print("(%d,%d): %d [%d,%d,%d,%d]" % (x,y,visibleB*visibleT*visibleR*visibleL,visibleT, visibleL, visibleB,visibleR))
        if maxiv<(visibleB * visibleT * visibleR * visibleL):
            maxiv=visibleB * visibleT * visibleR * visibleL

print("Max: %s" % maxiv)
