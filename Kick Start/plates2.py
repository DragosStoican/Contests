def maxi_func(beauty, stacks):
    maxil = []
    max_plate = 0
    for i in range(len(beauty)):
        if (beauty[i][0] > max_plate):
            max_plate = beauty[i][0]
            maxil.append(i)
    for i in maxil:
        stacks[i] += max_plate
        beauty[i] = beauty[i][1:]
    return max(stacks), len(stacks[maxil])

t = int(input())
maxi = [0 for i in range(t)]
for q in range(t):
    n, k, p = [int(s) for s in input().split(" ")]
    beauty = [[] for l in range(n)]
    for j in range(n):
        beauty[j] = [int(s) for s in input().split(" ")]
        stacks = [0 for i in range(n)]
    
    output = [0 for i in range(p)]
    for i in range(p):
        value, count = maxi_func(beauty, stacks)
        if(i - count < 0):
            output[i] = value
        else:
            output[i] = output[i-count-1] + value
    
    

for i in range(t):
    print("Case #" + str(i + 1) + ": " + str(maxi[i]))