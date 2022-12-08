inpFile = open("input.txt", "r").read().strip()
split1 = "\n"
if split1:
    inpFile = inpFile.split(split1)
for x in range(len(inpFile)):
    inpFile[x] = list(inpFile[x])

print(f"\n\n{inpFile}")
scoreDict = dict()


def checkSlices(row, col):
    height = int(inpFile[row][col])
    score = 1
    counter = 0
    for y in range(row-1, -1, -1):
        counter += 1
        if int(inpFile[y][col]) >= height:
            break
    score *= counter
    counter = 0
    for y in range(row+1, len(inpFile)):
        counter += 1
        if int(inpFile[y][col]) >= height:
            break
    score *= counter
    counter = 0
    for x in range(col-1, -1, -1):
        counter += 1
        if int(inpFile[row][x]) >= height:
            break
    score *= counter
    counter = 0
    for x in range(col+1, len(inpFile[0])):
        counter += 1
        if int(inpFile[row][x]) >= height:
            break
    score *= counter
    return score


for row in range(0, len(inpFile)):
    for col in range(0, len(inpFile[row])):
        if row == 0 or row == len(inpFile)-1 or col == 0 or col == len(inpFile[0])-1:
            pass
        else:
            scoreDict[f"{row}-{col}"] = checkSlices(row, col)
max = 0
for i in scoreDict.values():
    if i > max:
        max = i
print(max)
