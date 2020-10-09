def function(filename, outputname):
    f = open(filename, "r")
    g = open(outputname, "w")
    string = f.readline()
    string_lst = string.split()
    m = int(string_lst[0])
    n = int(string_lst[1])

    string = f.readline()
    string_lst = string.split()
    pizza_lst = []
    for i in string_lst:
        pizza_lst.append(int(i))
    

    dynamic_dict = dict()
    maxi = 0
    for j in range(n):
        aux = list(dynamic_dict.keys())
        for i in aux:
            value = i + pizza_lst[j]
            if (value <= m and value not in dynamic_dict):
                dynamic_dict[value] = dynamic_dict[i] + (j,)
                if (value > maxi):
                    maxi = value
        dynamic_dict[pizza_lst[j]] = (j,)
        print(maxi)


    g.write(str(len(dynamic_dict[maxi])) + "\n")
    for i in dynamic_dict[maxi]:
        g.write(str(i) + " ")
    g.close()




def function2(filename, outputname):
    f = open(filename, "r")
    g = open(outputname, "w")
    string = f.readline()
    string_lst = string.split()
    m = int(string_lst[0])
    n = int(string_lst[1])

    string = f.readline()
    string_lst = string.split()
    pizza_lst = []
    for i in string_lst:
        pizza_lst.append(int(i))
    
    s = 0
    pizzas = []
    p = len(pizza_lst) - 1
    while s + pizza_lst[p] < m:
        s += pizza_lst[p]
        pizzas.append(p)
        p -= 1
    
    p = 0
    while s + pizza_lst[p] < m:
        s += pizza_lst[p]
        pizzas.append(p)
        p += 1
    
    pizzas = sorted(pizzas)

    g.write(str(len(pizzas)) + "\n")
    for i in pizzas:
        g.write(str(i) + " ")
    g.close()




function("a_example.in", "a_exapmle.out")
function("b_small.in", "b_small.out")
function("c_medium.in", "c_medium.out")
function2("d_quite_big.in", "d_quite_big.out")
function2("e_also_big.in", "e_also_big.out")