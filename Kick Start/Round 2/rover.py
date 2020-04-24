t = int(input())
output = []
for k in range(t):
    program = input()
    north_south = 0
    east_west = 0
    last_nr = 1
    mult = 1
    for i in range(len(program)):
        step = program[i]
        if (step == "S"):
            north_south += 1 * mult
        elif (step == "N"):
            north_south -= 1 * mult
        elif (step == "E"):
            east_west += 1 * mult
        elif (step == "W"):
            east_west -= 1 * mult
        elif(step.isdecimal()):
            mult *= int(step)
            last_nr = int(step)
        elif (step == ")"):
            mult //= last_nr
            
    w = 1
    h = 1
    w += east_west
    h += north_south
    if (w <= 0):
        w = 1000000000 + w
    if (h <= 0):
        h = 1000000000 + h
    if (w > 1000000000):
        w = w - 1000000000
    if (h > 1000000000):
        h = h - 1000000000
    output.append((w,h))

for k in range(t):
    print("Case #{}: {} {}".format(k + 1, output[k][0], output[k][1]))
            