inpFile = open("input.txt", "r").read().strip()
split1 = "\n"
split2 = "\t"
if split1:
    inpFile = inpFile.split(split1)
if split2:
    for x in range(len(inpFile)):
        inpFile[x] = inpFile[x].split(split2)

print(f"\n\n{inpFile}")