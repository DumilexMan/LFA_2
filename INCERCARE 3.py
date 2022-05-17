f = open("input2.in", "r")

list_state = []
list_let = []
list_tra = []

list_aux = f.readlines()

n = int(list_aux[0])

line1 = list_aux[1]
line1 = line1[3:]

# reading the inputs

for aux in line1:
    if 'A' <= aux <= 'Z':
        list_state.append(aux)

line2 = list_aux[2]
line2 = line2[3:]

for aux in line2:
    if 'a' <= aux <= 'z':
        list_let.append(aux)

length_of_list = len(list_aux)

for index in range(3, length_of_list):
    aux = list_aux[index].replace("\n", "")
    list_tra.append(aux)

print(list_let)

mind = len(list_tra)

sol1 = [0] * (n+1)

def bkt1(k):
    global n, mind, sol1
    for v in list_let:
        sol1[k] = v
        if k == n:
            print(*sol1[1:], sep="")
        else:
            bkt1(k+1)

bkt1(1)

