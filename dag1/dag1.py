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
maxAmount = 0
for elf in inpFile:
    tot = 0
    for cal in elf:
        tot += int(cal)
    if tot > maxAmount:
        maxAmount = tot

print(maxAmount)
