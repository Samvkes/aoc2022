from functools import reduce

scoreDict = dict()
dirDict = dict()
def parseDirs(inhoud, dir):
    print(dir)
    score = 0
    for item in inhoud:
        if type(item) != tuple:
            if item in scoreDict:
                score += scoreDict[item]       
            else:
                scoreDict[item] = parseDirs(dirDict[item], f"{dir} \\ {item}")
                score += scoreDict[item]
        else:
            score += int(item[0])
    return score


inpFile = open("input.txt", "r").read().strip()
split1 = "\n"
split2 = "\t"
if split1:
    inpFile = inpFile.split(split1)
# if split2:
#     for x in range(len(inpFile)):
#         inpFile[x] = inpFile[x].split(split2)


print(f"\n\n{inpFile}")
dirList = []
curDir = ""
for line in inpFile:
    if dirList: totalDir = reduce(lambda x,y: x + "-" + y, dirList)
    if line == "$ cd ..":
        dirList.pop()
        curDir = dirList[-1]
    elif line[0:5] == "$ cd ":
        curDir = line[5:]    
        dirList.append(curDir)
    elif line[0:4] == "$ ls":
        pass
    elif line[0:4] == "dir ":
        if totalDir in dirDict:
            dirDict[totalDir].append(f"{totalDir}-{line[4:]}") 
        else:
            dirDict[totalDir] = [f"{totalDir}-{line[4:]}"]
    else:
        temp = line.split(" ")
        if totalDir in dirDict:
            dirDict[totalDir].append((temp[0], temp[1])) 
        else:
            dirDict[totalDir] = [(temp[0], temp[1])]

print(dirDict)

scoreDict['/'] = parseDirs(dirDict['/'], '/')
print(scoreDict)

target = 30000000 - (70000000 - scoreDict['/'])
smallest = 100000000
for size in scoreDict.values():
    if size >= target and size < smallest:
        smallest = size

print(smallest)