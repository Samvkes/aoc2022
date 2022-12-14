inpFile = open("input.txt", "r").read().strip()
split1 = "\n\n"
split2 = "\n"
if split1:
    inpFile = inpFile.split(split1)
if split2:
    for x in range(len(inpFile)):
        inpFile[x] = inpFile[x].split(split2)

#print(f"\n\n{inpFile}")
correct = 0

def listCheck(leftSide, rightSide):
    global correct
    #print(f"{leftSide=} {rightSide=}")
    cursor = 0
    while True:
        if len(leftSide) == cursor and len(rightSide) == cursor:
            return False
        elif len(leftSide) == cursor:
            correct += 1
            return True
        elif len(rightSide) == cursor:
            return True
        
        left = leftSide[cursor]
        right = rightSide[cursor]
        if type(left) == int and type(right) == int:
            if int(left) < int(right):
                correct += 1
                return True
            elif int(left) > int(right):
                return True
            else:
                cursor += 1
        elif type(left) == int and type(right) == list:
            leftSide[cursor] = [leftSide[cursor]]
            if listCheck(leftSide[cursor], rightSide[cursor]):
                return True
            else:
                cursor += 1
        elif type(left) == list and type(right) == int:
            rightSide[cursor] = [rightSide[cursor]]
            if listCheck(leftSide[cursor], rightSide[cursor]):
                return True
            else:
                cursor += 1
        else: 
            if listCheck(leftSide[cursor], rightSide[cursor]):
                return True
            else:
                cursor += 1

totList = ["[[2]]","[[6]]"]
for packet in inpFile:
    totList.append(packet[0])   
    totList.append(packet[1])   

while True:
    changed = False
    for i in range(0, len(totList)-1):
        leftSide = eval(totList[i])
        rightSide = eval(totList[i+1])
        oldCorrect = correct
        listCheck(leftSide, rightSide)
        if correct == oldCorrect:
            changed = True
            temp = totList[i]
            totList[i] = totList[i+1]
            totList[i+1] = temp         
    if not changed:
        break
    

counter = 0
twoPos = 0
sixPos = 0
for line in totList:
    counter += 1
    if line == "[[2]]":
        twoPos = counter
    if line == "[[6]]":
        sixPos = counter
        
print(twoPos * sixPos)