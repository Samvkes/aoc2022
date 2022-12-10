inpFile = open("input.txt", "r").read().strip()
split1 = "\n"
split2 = " "
if split1:
    inpFile = inpFile.split(split1)
if split2:
    for x in range(len(inpFile)):
        inpFile[x] = inpFile[x].split(split2)

reg = 0
def readIns(ins: list) -> int:
    tbd = 0
    if len(ins) == 1:
        return (0, tbd)        
    else:
        tbd = int(ins[1])
        return (1, tbd)


print(f"\n\n{inpFile}")
cycle = 1
reg = 1
cont = 0
sigStrength = 0
instruction = iter(inpFile)
tbd = 0
done = 0
counter = 1
print(len(inpFile))
while True:
    if not cont:
        reg += tbd
        try:
            counter += 1
            ins = next(instruction)
            out = readIns(ins)
            cont = out[0]
            tbd = out[1]
        except StopIteration:
            done = 1
    else:
        cont -= 1
    if cycle == 20 or (cycle - 20) % 40 == 0:
        sigStrength += cycle * reg
        print(counter)
        print(ins)
        print(cycle * reg)
        print(f"{sigStrength=} {cycle=} {reg=}")
    if done == 1: break
    cycle += 1
print(sigStrength)
