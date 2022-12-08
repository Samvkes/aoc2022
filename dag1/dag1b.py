inpFile = open("input.txt", "r").read().strip()
split1 = "\n\n"
split2 = "\n"
if split1:
    inpFile = inpFile.split(split1)
if split2:
    for x in range(len(inpFile)):
        inpFile[x] = inpFile[x].split(split2)

print("\n\n")
print(inpFile)
amountList = []
for elf in inpFile:
    tot = 0
    for cal in elf:
        tot += int(cal)
    amountList.append(tot)

amountList.sort(reverse=True)
print(amountList[0])
print(amountList[1])
print(amountList[2])
print(amountList[0] + amountList[1] + amountList[2])
