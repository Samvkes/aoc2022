inpFile = open("input.txt", "r").read().strip()
split1 = "\n"
if split1:
    inpFile = inpFile.split(split1)

outComeDict = {
    "A X" : 4,
    "A Y" : 8,
    "A Z" : 3,
    "B X" : 1,
    "B Y" : 5,
    "B Z" : 9,
    "C X" : 7,
    "C Y" : 2,
    "C Z" : 6,
}

score = 0
for round in inpFile:
    score += outComeDict[round]

print(score)