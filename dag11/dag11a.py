class Monkey:
    def __init__(self, number, items, inspect, test, ifTrue, ifFalse):
        self.number = number
        self.items = items
        self.inspect = inspect
        self.test = test
        self.ifTrue = ifTrue
        self.ifFalse = ifFalse
        self.inspected = 0

    def inspectItem(self, item):
        self.inspected += 1
        if len(self.inspect) == 1:
            item = item * item
        elif self.inspect[0] == "+":
            item = item + self.inspect[1]
        elif self.inspect[0] == "*":
            item = item * self.inspect[1]
        else:
            raise ValueError("geen plus of keer")
        item = item // 3
        return item

    def turn(self, monkeys):
        while True:
            if len(self.items) == 0:
                break
            toThrow = self.items.pop(0)
            toThrow = self.inspectItem(toThrow)
            if toThrow % self.test == 0:
                monkeys[self.ifTrue].collect(toThrow)
            else:
                monkeys[self.ifFalse].collect(toThrow)

    def collect(self, item):
        self.items.append(item)


inpFile = open("input.txt", "r").read().strip()
split1 = "\n\n"
split2 = "\n"
if split1:
    inpFile = inpFile.split(split1)
if split2:
    for x in range(len(inpFile)):
        inpFile[x] = inpFile[x].split(split2)

print(f"\n\n{inpFile}")

monkeyList = []
for monk in inpFile:
    num = int(monk[0][-2])  
    items = monk[1][17:].split(',')
    items = [int(x.strip()) for x in items]
    inspect = monk[2].split(' ')
    if inspect[-1] == "old":
         inspect = ["square"]
    else:
        inspect = [inspect[-2], int(inspect[-1])]
    test = int(monk[3].split(' ')[-1])
    ifTrue = int(monk[4].split(' ')[-1])
    ifFalse = int(monk[5].split(' ')[-1])
    monkeyList.append(Monkey(num, items, inspect, test, ifTrue, ifFalse))

for x in range(20):
    for monkey in monkeyList:
        monkey.turn(monkeyList)
        
maxList = []
for monkey in monkeyList:
    maxList.append(monkey.inspected)
maxList.sort(reverse=True)
print(maxList[0] * maxList[1])
