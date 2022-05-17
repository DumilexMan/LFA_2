f = open("input.in", "r")

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


# processing possibilities

# max index of path
mind = len(list_tra)
list_pos = []
list_pos_aux = []
list_pos_aux1 = []
sol = [0] * (n)

print(mind)
print(n)


def bkt(k):
    global mind, n, sol, list_pos
    for v in range(0,mind):
        sol[k] = v
        if k == n-1:
            # print(sol)
            aux = sol.copy()
            # print(aux)
            list_pos_aux1.append(aux)
        else:
            bkt(k+1)


bkt(0)

# verifying if a posibility is compatible #1

#print(list_tra)

for aux in list_pos_aux1:
    index = aux[-1]
    if list_tra[index].find('~') != -1 :
        list_pos_aux.append(aux)


# print(list_pos)


# list_words=[]

for aux in list_pos_aux:
    for index in aux:
        if list_tra[index][0] == 'S' :
            list_pos.append(aux)

print(list_pos)

# true list of possible index

#list_pos_ok = []

#for index in list_pos:
#    ok = 1
#    # print(index)
#    for index_aux in range(0,len(index)-1):
#        # print(list_tra[index[index_aux]])
#        aux_list = list_tra[index[index_aux]][4:]
#        for letter in aux_list:
#            if 'a' <= letter <= 'b':
#                aux_list=aux_list.replace( letter, "")
#        # print(aux_list)
#        if list_tra[index[index_aux+1]].find(aux_list):
#            print("da",list_tra[index[index_aux]], " " ,list_tra[index[index_aux+1]], " " ,index)

# finding words


# print(n)
# print(list_let)
# print(list_tra)


# processing


sol1 = [0] * (n+1)

words=[]

def bkt1(k):
    global n, mind, sol1
    for v in list_let:
        sol1[k] = v
        if k == n:
            aux1=sol1[1:].copy()
            aux2=""
            for aa in aux1:
                aux2=aux2+aa
            words.append(aux2)
            # print(aux2)
        else:
            bkt1(k+1)


bkt1(1)


print(words)

nr = 0

for word in words:
    ok = 0
    for letter in word:

        for aux in list_pos:
            for index in aux:
                if list_tra[index].find(word):
                    ok = 1
                    break
                if ok == 1:
                    break
                    # print(list_tra[index])
    if ok == 1 and nr < n:
        nr = nr + 1
        print(word)

print(list_tra)

for cont in range(len(list_pos)):
    for aux in list_pos:
        for aux1 in aux:
            for i in list_tra[aux1]:
                if 'A' <= i <= 'Z':
                    let = i
            if list_tra[aux1].find('~') == -1:
                print(list_tra[aux1][4:].replace(let, ""), end = "")
    print("")
