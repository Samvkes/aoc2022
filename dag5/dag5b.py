def parseCrates(crates: list) -> list:
    outList = []
    for x in range(9):
        outList.append([])
    for row in range(len(crates)-1, -1, -1):
        for step in range(0, len(crates[row]), 4):
            if crates[row][step] == '[':
                outList[int((step / 4))].append(crates[row][step+1])
            else:
                pass
    return outList

def moveCrates(crates,instructions):
    for line in instructions:
        line = line.strip("move ")
        line = line.replace(" from ", "-")
        line = line.replace(" to ", "-")
        line = line.split("-")
        print(line)
        amount = int(line[0])
        fromRow = int(line[1]) - 1
        toRow = int(line[2]) - 1
        tempList = []
        for i in range(amount):
            tempList.append(crates[fromRow].pop(-1))
        tempList.reverse()
        crates[toRow].extend(tempList)
    return crates

inpFile = open("input.txt", "r").read()
split1 = "\n\n"
split2 = "\n"
if split1:
    inpFile = inpFile.split(split1)
if split2:
    for x in range(len(inpFile)):
        inpFile[x] = inpFile[x].split(split2)
print(inpFile)
crates = parseCrates(inpFile[0])
movedCrates = moveCrates(crates, inpFile[1])

print(f"\n\n{crates}\n{movedCrates}")
for row in movedCrates:
    print(row[-1])