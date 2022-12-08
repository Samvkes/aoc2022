inpFile = open("input.txt", "r").read().strip()
split1 = "\n"
if split1:
    inpFile = inpFile.split(split1)
for x in range(len(inpFile)):
    inpFile[x] = list(inpFile[x])

print(f"\n\n{inpFile}")
visibleDict = dict()


def checkSlices(row, col):
    height = int(inpFile[row][col])
    obscured = 0
    for y in range(row-1, -1, -1):
        if int(inpFile[y][col]) >= height:
            obscured = 1
            break
    if not obscured: return True
    obscured = 0
    for y in range(row+1, len(inpFile)):
        if int(inpFile[y][col]) >= height:
            obscured = 1
            break
    if not obscured: return True
    obscured = 0
    for x in range(col-1, -1, -1):
        if int(inpFile[row][x]) >= height:
            obscured = 1
            break
    if not obscured: return True
    obscured = 0
    for x in range(col+1, len(inpFile[0])):
        if int(inpFile[row][x]) >= height:
            obscured = 1
            break
    if not obscured: return True
    return False


for row in range(0, len(inpFile)):
    for col in range(0, len(inpFile[row])):
        if row == 0 or row == len(inpFile)-1 or col == 0 or col == len(inpFile[0])-1:
            visibleDict[f"{row}-{col}"] = True
        else:
            visibleDict[f"{row}-{col}"] = checkSlices(row, col)

visCount = 0
for i in visibleDict.values():
    if i: visCount += 1
print(len(inpFile))
print(visCount)
