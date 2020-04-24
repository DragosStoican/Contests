t = int(input())
output = [0 for i in range(t)]
for k in range(t):
    n, d = [int(s) for s in input().split(" ")]
    buses = [int(s) for s in input().split(" ")]
    b1 = buses[0]
    while (b1 <= d):
        days = b1
        for i in range(1,n):
            x = buses[i]
            while (x < days):
                x += buses[i]
            days = x
        if (days <= d):
            output[k] = b1
        b1 += buses[0]
        
        


for k in range(t):
    print("Case #{}: {}".format(k + 1, output[k]))
        
        
