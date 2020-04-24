t = int(input())
output = [0 for i in range(t)]
for p in range(t):
    n = int(input())
    lst = [int(s) for s in input().split(" ")]
    x = lst[0]
    y = lst[1]
    for i in range(2, n):
        z = lst[i]
        if (x < y and y > z):
            output[p] += 1
        x = y
        y = z

for x in range(t):
    print("Case #{}: {}".format(x + 1, output[x]))