def findRepeats(stream: str) -> int:
    cursor = 14
    buffer = list(stream[0:cursor])
    if len(set(buffer)) == len(buffer):
        return cursor
    while True:
        buffer.pop(0)
        buffer.append(stream[cursor])
        cursor += 1
        if len(set(buffer)) == len(buffer):
            return cursor


inpFile = open("input.txt", "r").read().strip()

print(f"\n\n{inpFile}")
print(findRepeats(inpFile))

