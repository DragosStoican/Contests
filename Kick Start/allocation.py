t = int(input())
nr_houses = [0 for i in range(t)]
for i in range(t):
    n, b = [int(s) for s in input().split(" ")]
    costs = [int(s) for s in input().split(" ")]
    costs = sorted(costs)
    value = 0
    for house in costs:
        if (house + value <= b):
            value += house
            nr_houses[i] += 1
        else:
            break

for i in range(t):
    print("Case #" + str(i + 1) + ": " + str(nr_houses[i]))