import re
inpFile = open("test.txt", "r").read().strip()
split1 = "\n"
if split1:
    inpFile = inpFile.split(split1)

target = 20
li = []
for line in inpFile:
    ex = re.findall("x=[^,]*", line)
    ey = re.findall("y=[^:]*", line)
    li.append((ex, ey))

def distance(sens, possibles):
    newPossibles = set()
    xcoord = sens[0][0]
    ycoord = sens[0][1]
    dist = abs(sens[0][0] - sens[1][0]) + abs(sens[0][1] - sens[1][1])
    for possible in possibles:
        if (abs(sens[0][0] - possible[0]) + abs(sens[0][1] - possible[1])) <= dist:
            pass
        else:
            newPossibles.add(possible)
    return newPossibles
            
    
    
def cirkel(sens, target):
    xcoord = sens[0][0]
    ycoord = sens[0][1]
    global possibles
    dist = abs(sens[0][0] - sens[1][0]) + abs(sens[0][1] - sens[1][1])
    dist += 1
    for x in range(dist):
        y = dist - x                    
        if 0 <= xcoord + x <= target and 0 <= ycoord + y <= target: 
            possibles.add((xcoord + x, ycoord + y))
    for x in range(0, -dist, -1):
        y = dist + x
        if 0 <= xcoord + x <= target and 0 <= ycoord + y <= target: 
            possibles.add((xcoord + x, ycoord + y))
    for x in range(dist):
        y = -dist + x                    
        if 0 <= xcoord + x <= target and 0 <= ycoord + y <= target: 
            possibles.add((xcoord + x, ycoord + y))
    for x in range(0, -dist, -1):
        y = -dist - x
        if 0 <= xcoord + x <= target and 0 <= ycoord + y <= target: 
            possibles.add((xcoord + x, ycoord + y))
        
sensorsInTarget = set()
beaconsInTarget = set()
lir = []
for sensor in li:
    sx = int(sensor[0][0].split("=")[1])
    sy = int(sensor[1][0].split("=")[1])
    bx = int(sensor[0][1].split("=")[1])
    by = int(sensor[1][1].split("=")[1])
    lir.append(((sx,sy), (bx,by)))

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
possibles = set()


for sensor in lir:
    print(sensor)
    cirkel(sensor, target)
# canvas = ""
# for y in range(20):
#     for x in range(maxRight):
#         ja = False
#         for poss in possibles:
#             if x == poss[0] and y == poss[1]:
#                 ja = True
#         if ja == True:
#             canvas += "*"
#         else: 
#             canvas += "."
#     canvas += "\n"
# print(canvas)
for sensor in lir:
    print(len(possibles))
    print(sensor)
    possibles = distance(sensor, possibles)

counter = 0
print(f"{len(beaconsInTarget)=} {len(sensorsInTarget)=}")
found = possibles.pop()
print((found[0] * 4000000) + found[1])
