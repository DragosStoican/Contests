def recursive(line, beauty, max_line, plates, max_plates):
    if (line == max_line):
        if (max_plates - plates < len(beauty[line])):
            return beauty[line][max_plates - plates]
        else:
            return 0
    else:
        maxi = 0
        for i in range(0, min(len(beauty[line]), max_plates - plates + 1)):
            s = beauty[line][i] + recursive(line + 1, beauty, max_line, plates + i, max_plates)
            if (s > maxi):
                maxi = s
        return maxi

t = int(input())
maxi = [0 for i in range(t)]
for q in range(t):
    n, k, p = [int(s) for s in input().split(" ")]
    beauty = [[0 for l in range(k + 1)]] + [[] for l in range(n)]
    for j in range(1, n + 1):
        aux = [0] + [int(s) for s in input().split(" ")]
        beauty[j].append(0)
        for l in range(1, k + 1):
            beauty[j].append(beauty[j][l - 1] + aux[l])
    
    maxi[q] = recursive(1, beauty, n, 0, p)

for i in range(t):
    print("Case #" + str(i + 1) + ": " + str(maxi[i]))