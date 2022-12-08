def score(let):
    let = let.pop()
    if ord(let) - 96 > 0:
        return ord(let) - 96
    else:
        return ord(let) - 65 + 27


inpFile = open("input.txt", "r").read().strip()
split1 = "\n"
if split1:
    inpFile = inpFile.split(split1)

pList = []
for sack in inpFile:
    halfw = int(len(sack)/2)
    p1 = set(sack[0:halfw])
    p2 = set(sack[halfw:])
    print(p1.intersection(p2))
    pList.append(p1.intersection(p2))

total = 0
for x in pList:
    total += score(x)

print(total)
