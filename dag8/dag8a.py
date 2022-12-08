inpFile = open("input.txt", "r").read().strip()
split1 = "\n"
if split1:
    inpFile = inpFile.split(split1)
for x in range(len(inpFile)):
    inpFile[x] = list(inpFile[x])

print(f"\n\n{inpFile}")

visibleDict = dict()
def isVisible(row, col):
    print(visibleDict)
    print((row, col))
    height = int(inpFile[row][col])
    if row == 0 or row == len(inpFile) - 1 or col == 0 or col == len(inpFile[row]) - 1:
        visibleDict[f"{row}-{col}"] = (True, int(inpFile[row][col]))
        return
    for y in range(row-1, -1, -1):
        if f"{y}-{col}" in visibleDict:
            if visibleDict[f"{y}-{col}"][0] and visibleDict[f"{y}-{col}"][1] < height:
                visibleDict[f"{row}-{col}"] = (True, height)
                return
            else:
                break
        else:
            isVisible(y, col)
            if visibleDict[f"{y}-{col}"][0] and visibleDict[f"{y}-{col}"][1] < height:
                visibleDict[f"{row}-{col}"] = (True, height)
                return
    for y in range(row+1, len(inpFile)):
        if f"{y}-{col}" in visibleDict:
            if visibleDict[f"{y}-{col}"][0] and visibleDict[f"{y}-{col}"][1] < height:
                visibleDict[f"{row}-{col}"] = (True, height)
                return
            else:
                break
        else:
            isVisible(y, col)
            if visibleDict[f"{y}-{col}"][0] and visibleDict[f"{y}-{col}"][1] < height:
                visibleDict[f"{row}-{col}"] = (True, height)
                return
    for x in range(col-1, -1, -1):
        if f"{row}-{x}" in visibleDict:
            if visibleDict[f"{row}-{x}"][0] and visibleDict[f"{row}-{x}"][1] < height:
                visibleDict[f"{row}-{col}"] = (True, height)
                return
            else:
                break
        else:
            isVisible(row, x)
            if visibleDict[f"{row}-{x}"][0] and visibleDict[f"{row}-{x}"][1] < height:
                visibleDict[f"{row}-{col}"] = (True, height)
                return
    for x in range(col+1, len(inpFile[0])):
        if f"{row}-{x}" in visibleDict:
            if visibleDict[f"{row}-{x}"][0] and visibleDict[f"{row}-{x}"][1] < height:
                visibleDict[f"{row}-{col}"] = (True, height)
                return
            else:
                break
        else:
            isVisible(row, x)
            if visibleDict[f"{row}-{x}"][0] and visibleDict[f"{row}-{x}"][1] < height:
                visibleDict[f"{row}-{col}"] = (True, height)
                return
    visibleDict[f"{row}-{col}"] = (False, height)
    return 


for row in range(len(inpFile)):
    for col in range(len(inpFile[row])):
        if row == 0 or row == len(inpFile) - 1 or col == 0 or col == len(inpFile[row]) - 1:
            visibleDict[f"{row}-{col}"] = (True, int(inpFile[row][col]))
        elif f"{row}-{col}" in visibleDict:
            pass
        else:
            isVisible(row, col)
print(visibleDict)