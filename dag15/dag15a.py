import re
inpFile = open("input.txt", "r").read().strip()
split1 = "\n"
if split1:
    inpFile = inpFile.split(split1)

targetLine = 2000000
li = []
for line in inpFile:
    ex = re.findall("x=[^,]*", line)
    ey = re.findall("y=[^:]*", line)
    li.append((ex, ey))


def howMuch(sens, target):
    global theRow
    dist = abs(sens[0][0] - sens[1][0]) + abs(sens[0][1] - sens[1][1])
    tdist = abs(target - sens[0][1])
    amount = (dist - tdist) * 2 + 1 
    if amount <= 0:
        return
    side = amount // 2
    for i in range(amount):
        num = sens[0][0] - side + i
        theRow[num] = "#"
        
        
sensorsInTarget = set()
beaconsInTarget = set()
lir = []
for sensor in li:
    sx = int(sensor[0][0].split("=")[1])
    sy = int(sensor[1][0].split("=")[1])
    bx = int(sensor[0][1].split("=")[1])
    by = int(sensor[1][1].split("=")[1])
    lir.append(((sx,sy), (bx,by)))
    if sy == targetLine:
        sensorsInTarget.add(sx) 
    if by == targetLine:
        beaconsInTarget.add(bx)

print(f"\n\n{lir}")
maxLeft = 0
maxRight = 0
for sensor in lir:
    if sensor[0][0] < maxLeft:
        maxLeft = sensor[0][0]
    if sensor[1][0] < maxLeft:
        maxLeft = sensor[1][0]
    if sensor[0][1] > maxRight:
        maxRight = sensor[0][1]
    if sensor[1][1] > maxRight:
        maxRight = sensor[1][1]

print(f"{maxLeft=} {maxRight=}")
theRow = dict()


for sensor in lir:
    howMuch(sensor, targetLine)
counter = 0
for a in theRow:
    # if a < maxLeft or a > maxRight:
    #     pass
    # else:
    #     counter += 1
    counter += 1
print(counter)
print(f"{len(beaconsInTarget)=} {len(sensorsInTarget)=}")
