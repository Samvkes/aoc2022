inpFile = open("input.txt", "r").read().strip()
split1 = "\n"
if split1:
    inpFile = inpFile.split(split1)
for x in range(len(inpFile)):
    inpFile[x] = list(inpFile[x])

print(f"\n\n{inpFile}")
visibleDict = dict()


def doPass(visibleDict):
    for y in range(1, len(inpFile)-1):
        for x in range(1, len(inpFile[0])-1):
            height = int(inpFile[y][x])
            # print(height)
            # print(f"{y=} {x=}")
            if f"{y}-{x}" in visibleDict:
                pass
            else:
                if f"{y-1}-{x}" in visibleDict:
                    if visibleDict[f"{y-1}-{x}"][0] and visibleDict[f"{y-1}-{x}"][1] < height:
                        visibleDict[f"{y}-{x}"] = (True, height)
                if f"{y+1}-{x}" in visibleDict:
                    if visibleDict[f"{y+1}-{x}"][0] and visibleDict[f"{y+1}-{x}"][1] < height:
                        visibleDict[f"{y}-{x}"] = (True, height)
                if f"{y}-{x-1}" in visibleDict:
                    if visibleDict[f"{y}-{x-1}"][0] and visibleDict[f"{y}-{x-1}"][1] < height:
                        visibleDict[f"{y}-{x}"] = (True, height)
                if f"{y}-{x+1}" in visibleDict:
                    if visibleDict[f"{y}-{x+1}"][0] and visibleDict[f"{y}-{x+1}"][1] < height:
                        visibleDict[f"{y}-{x}"] = (True, height)
    return visibleDict


for row in range(len(inpFile)):
    for col in range(len(inpFile[row])):
        if row == 0 or row == len(inpFile) - 1 or col == 0 or col == len(inpFile[row]) - 1:
            visibleDict[f"{row}-{col}"] = (True, int(inpFile[row][col]))

for x in range(100):
    visibleDict = doPass(visibleDict)
    print(len(visibleDict))

print(visibleDict)
