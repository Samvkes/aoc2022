inpFile = open("input.txt", "r").read().strip()
split1 = "\n"
if split1:
    inpFile = inpFile.split(split1)
for x in range(len(inpFile)):
    inpFile[x] = list(inpFile[x])

##print(f"\n\n{inpFile}")

maxLengthY = len(inpFile)
maxLengthX = len(inpFile[0])
start = "S"
target = "E"
possible = list()
startLoc = ()
for y in range(len(inpFile)):
    for x in range(len(inpFile[y])):
        if inpFile[y][x] == start:
            startLoc = (x,y)
        if inpFile[y][x] == target:
            targetLoc = (x,y)
        if inpFile[y][x] == "a":
            possible.append((x,y))


def getNeighbours(loc):
    ##print(f"getNeighbours({loc=})")
    outList = []
    preList = [
        (loc[0]-1, loc[1]),
        (loc[0]+1, loc[1]),
        (loc[0], loc[1]-1),
        (loc[0], loc[1]+1)
    ]
    for candidate in preList:
        if (candidate[0] >= maxLengthX or candidate[0] < 1) or (candidate[1] >= maxLengthY or candidate[1] < 0):
            continue
        elif inpFile[candidate[1]][candidate[0]] == "E" and inpFile[loc[1]][loc[0]] != "z":
            continue
        elif ord((inpFile[candidate[1]][candidate[0]]).lower())-1 > ord((inpFile[loc[1]][loc[0]]).lower()) :
            continue
        else:
            outList.append(candidate)
    ##print(f"{outList=}")
    return outList


cameFrom = dict()
frontier = list()
reached = set()
reached.add(str(startLoc))
frontier.append(startLoc)
done = 0
c = 0
while True:
    c += 1
    #print(c)
    if c == 100000:
        #print("telang")
        break
    ##print(f"{reached=}")
    if frontier:
        ##print(f"{frontier=}")
        current = frontier.pop(0)
        neighbours = getNeighbours(current)
        for nb in neighbours:
            if str(nb) not in reached:
                ##print(f"{nb=}")
                ##print(inpFile[nb[1]][nb[0]])
                reached.add(str(nb))
                cameFrom[str(nb)] = str(current)
                #print(cameFrom)
                frontier.append(nb)
                if inpFile[nb[1]][nb[0]] == target:
                    #print("yes!!")
                    done = 1
                    break
    if done == 1:
        break

#print("gehaald")
counter = 0
cur = str(targetLoc)
toDraw = []
countDict = dict()
while True:
    ##print(cur)
    if counter == 5000:
        #print("telang")
        break
    if cur in cameFrom:
        countDict[cur] = counter
        toDraw.append(cur)
        #print(cur)
        cur = cameFrom[cur]
        counter += 1
    else:
        print(counter)
        break

# #print(len(toDraw))
# #print(len(set(toDraw)))
# letList=list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
# #print(countDict)
# drawing = ""
# for y in range(maxLengthY):
#     for x in range(maxLengthX):
#         yes = 0
#         for item in toDraw:
#             it = item
#             item = item.lstrip("(").rstrip(")").split(",")
#             if int(item[0].strip()) == x and int(item[1].strip()) == y:
#                 yes = 1
#                 et = it
#         item = [int(item[0].strip()), int(item[1].strip())]
#         if yes ==1:
#             #print(et)
#             drawing += f"\033[91m{inpFile[y][x]}\033[39m"
#         else:
#             drawing += inpFile[y][x]
#     drawing += "\n"
# print(drawing)
