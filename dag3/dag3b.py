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
inpFile = iter(inpFile)
while True:
    try:
        p1 = set(next(inpFile))
        p2 = set(next(inpFile))
        p3 = set(next(inpFile))
    except StopIteration:
        break
    same = p1.intersection(p2.intersection(p3))
    pList.append(same)

total = 0
for x in pList:
    total += score(x)

print(total)
