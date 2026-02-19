with open("input.txt") as f:
    lines = f.readlines()

pos = 50
count = 0

for line in lines:
    line = line.strip()
    if line == "":
        continue

    direction = line[0]
    n = int(line[1:])

    if direction == "R":
        pos = pos + n
    else:
        pos = pos - n

    # wrap around
    pos = pos % 100

    if pos == 0:
        count += 1

print(count)
