def hl(list):
    return f"{list[0]}-{list[1]}"


inpFile = open("input.txt", "r").read().strip()
split1 = "\n"
split2 = " "
if split1:
    inpFile = inpFile.split(split1)
if split2:
    for x in range(len(inpFile)):
        inpFile[x] = inpFile[x].split(split2)

print(f"\n\n{inpFile}")
head = [0,0]
tail = [0,0]
beenSet = {hl(head)}


def tailMove(head, tail):
    if abs(head[0] - tail[0]) <= 1 and abs(head[1] - tail[1]) <= 1:
        return (0,0)
    if head[0] - tail[0] == 0 and head[1] - tail[1] == 2:
        return (0,1)
    if head[0] - tail[0] == 0 and head[1] - tail[1] == -2:
        return (0,-1)
    if head[0] - tail[0] == 2 and head[1] - tail[1] == 0:
        return (1,0)
    if head[0] - tail[0] == -2 and head[1] - tail[1] == 0:
        return (-1,0)
    if (head[0] - tail[0] == -2 and head[1] - tail[1] == 1) or (head[0] - tail[0] == -1 and head[1] - tail[1] == 2):
        return (-1,1)
    if (head[0] - tail[0] == 2 and head[1] - tail[1] == -1) or (head[0] - tail[0] == 1 and head[1] - tail[1] == -2):
        return (1,-1)
    if (head[0] - tail[0] == -2 and head[1] - tail[1] == -1) or (head[0] - tail[0] == -1 and head[1] - tail[1] == -2):
        return (-1,-1)
    if (head[0] - tail[0] == 2 and head[1] - tail[1] == 1) or (head[0] - tail[0] == 1 and head[1] - tail[1] == 2):
        return (1,1)
    print("error")


for line in inpFile:
    print(line)
    headChange = (0,0)
    if line[0] == "R":
        headChange = (1,0)
    if line[0] == "L":
        headChange = (-1,0)
    if line[0] == "U":
        headChange = (0,1)
    if line[0] == "D":
        headChange = (0,-1)
    for i in range(int(line[1])):
        print(f"{head=} {tail=}")
        head[0] += headChange[0]
        head[1] += headChange[1]
        tailChange = tailMove(head, tail)
        tail[0] += tailChange[0]
        tail[1] += tailChange[1]
        beenSet.add(hl(tail))

print(len(beenSet))
