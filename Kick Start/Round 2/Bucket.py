def rec_check(days, lst, i, d):
    x = lst[i]
    while (x < days):
        x += lst[i]
    if (i == len(lst) - 1 and x <= d):
        return True
    elif (i == len(lst) - 1 and x > d):
        return False
    return rec_check(x, lst, i+1, d)
            

t = int(input())
output = [0 for i in range(t)]
for k in range(t):
    n, d = [int(s) for s in input().split(" ")]
    buses = [int(s) for s in input().split(" ")]
    b1 = buses[0]
    maxi = -1
    while (b1 <= d):
        if (n == 1 or rec_check(b1, buses, 1, d)):
            maxi = b1
        b1 += buses[0]
    output[k] = maxi


for x in range(t):
    print("Case #{}: {}".format(x + 1, output[x]))
        
        
