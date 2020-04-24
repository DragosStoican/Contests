def parantheses(program):
    translate = ""
    while (program != ""):
        step = program[0]
        if (step == "S"):
            translate += step
        elif (step == "N"):
            translate += step
        elif (step == "E"):
            translate += step
        elif (step == "W"):
            translate += step
        elif(step.isdecimal()):
            temp = parantheses(program[2 :])
            translate += temp * int(step)
            program = program[len(temp) + 2 :]
        elif (step == ")"):
            return translate
        program = program[1:]
    return translate

t = int(input())
output = []
for k in range(t):
    program = input()
    translate = parantheses(program)
    

    w = 1
    h = 1
    for letter in translate:
        if (letter == "S"):
            h += 1
            if (h > 1000000000):
                h = h - 1000000000
        elif (letter == "N"):
            h -= 1
            if (h <= 0):
                h = 1000000000 + h
        if (letter == "E"):
            w += 1
            if (w > 1000000000):
                w = w - 1000000000
        elif (letter == "W"):
            w -= 1
            if (w <= 0):
                w = 1000000000 + w

    output.append((w,h))

for k in range(t):
    print("Case #{}: {} {}".format(k + 1, output[k][0], output[k][1]))
            