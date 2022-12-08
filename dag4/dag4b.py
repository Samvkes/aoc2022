inpFile = open("input.txt", "r").read().strip()
split1 = "\n"
split2 = ","
if split1:
    inpFile = inpFile.split(split1)
if split2:
    for x in range(len(inpFile)):
        inpFile[x] = inpFile[x].split(split2)

counter = 0
for pair in inpFile:
    elf1 = pair[0].split('-')
    elf2 = pair[1].split('-')
    set1 = set(range(int(elf1[0]), int(elf1[1])+1))
    set2 = set(range(int(elf2[0]), int(elf2[1])+1))
    together = set1.union(set2)
    if len(together) != len(set1) + len(set2):
        counter += 1

print(counter)