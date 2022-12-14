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

total = 0
indice = 0
for packet in inpFile:
    indice += 1
    leftSide = eval(packet[0])
    rightSide = eval(packet[1])
    leftListLev = 0
    rightListLev = 0
    cursor = 0
    oldCorrect = correct
    #print(leftSide)
    #print(rightSide)
    listCheck(leftSide, rightSide)
    if correct > oldCorrect:
        #print(f"{indice} is correct!")
        total += indice
                
    
    
print(total)