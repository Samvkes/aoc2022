inpFile = open("input.txt", "r").read().strip()
split1 = "\n"
split2 = ""
if split1:
    inpFile = inpFile.split(split1)
if split2:
    for x in range(len(inpFile)):
        inpFile[x] = inpFile[x].split(split2)

print(f"\n\n{inpFile}")

outComeDict = {
    "A X" : 3,
    "A Y" : 4,
    "A Z" : 8,
    "B X" : 1,
    "B Y" : 5,
    "B Z" : 9,
    "C X" : 2,
    "C Y" : 6,
    "C Z" : 7,
}

score = 0
for round in inpFile:
    score += outComeDict[round]

print(score)