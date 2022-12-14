inpFile = open("test.txt", "r").read().strip()
split1 = "\n"
split2 = " -> "
if split1:
    inpFile = inpFile.split(split1)
if split2:
    for x in range(len(inpFile)):
        inpFile[x] = inpFile[x].split(split2)
        for y in range(len(inpFile[x])):
            inpFile[x][y] = inpFile[x][y].split(",")
            inpFile[x][y][0] = int(inpFile[x][y][0])
            inpFile[x][y][1] = int(inpFile[x][y][1])


def dropSand():
    global gridList
    global maxLeft
    ml = maxLeft
    sand = [0, 500 - ml]
    while True:
        try:
            if not gridList[sand[0] + 1][sand[1]]:
                sand[0] += 1
            elif not gridList[sand[0] + 1][sand[1] - 1]:
                sand[0] += 1
                sand[1] -= 1
            elif not gridList[sand[0] + 1][sand[1] + 1]:
                sand[0] += 1
                sand[1] += 1
            else:
                break
        except IndexError:
            return 2
    if sand[0] == 0 and sand[1] == 500 - ml:
        return 1 
    gridList[sand[0]][sand[1]] = 2
    return 0


def drawGrid(gridList):
    canvas = ""
    for row in gridList:
        drawnRow = ""
        for mark in row:
            if not mark:
                drawnRow += "."
            elif mark == 1:
                drawnRow += "#"
            elif mark == 2:
                drawnRow += "o"
            else:
                print("ERROR")
        drawnRow += "\n"
        canvas += drawnRow
    print(canvas)    

    
print(f"\n\n{inpFile}")
maxDepth = 0
maxLeft = 500
maxRight = 500
for line in inpFile:
    for coord in line:
        if coord[0] <= 500:
            if coord[0] < maxLeft:
                maxLeft = coord[0]
        else:
            if coord[0] > maxRight:
                maxRight = coord[0]
        if coord[1] > maxDepth:
            maxDepth = coord[1]

expand = 300
inpFile.append([[maxLeft - expand, maxDepth + 2], [maxRight + expand, maxDepth + 2]])
maxLeft = maxLeft - expand
maxRight = maxRight + expand
maxDepth = maxDepth + 2

print(f"{maxDepth=} {maxLeft=} {maxRight=}")
gridList = []
for y in range(maxDepth + 1):
    col = []
    for x in range((maxRight - maxLeft) + 1):
        col.append(0)
    gridList.append(col)

drawGrid(gridList)
    
print(len(gridList))
print(len(gridList[0]))
for line in inpFile:
    for coord in range(len(line) -1):
        ax = line[coord][0]
        ay = line[coord][1]
        bx = line[coord+1][0]
        by = line[coord+1][1]
        print(f"{ax=} {ay=} {bx=} {by=}")
        if line[coord][0] == line[coord+1][0]:
            if ay < by:
                for y in range(ay, by + 1):
                    gridList[y][ax-maxLeft] = 1 
            if ay > by:
                for y in range(ay, by - 1, -1):
                    gridList[y][ax-maxLeft] = 1 
        if line[coord][1] == line[coord+1][1]:
            if ax < bx:
                for x in range(ax, bx + 1):
                    gridList[ay][x-maxLeft] = 1 
            if ax > bx:
                for x in range(ax, bx - 1, -1):
                    gridList[ay][x-maxLeft] = 1 
drawGrid(gridList)

antwoord = 0
for i in range(100000):
    uitkomst = dropSand()
    if uitkomst == 1:
        antwoord = i
        break
    elif uitkomst == 2:
        print("foutje")

drawGrid(gridList)
print(f"Klaar! {antwoord=}")
