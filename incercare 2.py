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


def word():
    nr=0
    print(list_tra)
    for i in list_tra:
        cuv = ""
        if i[0] == 'S':
            # print(i)
            aux = i[4:]
            # print(aux)
            for letter in aux:
                if 'A' <= letter <= 'Z':
                    letter_aux=letter
            # print(letter_aux)
            cuv=aux.replace(letter,cuv)
            print(cuv)
            nr = len(cuv)
            for j in list_tra:
                if j.find(letter) != -1:
                    for letter in aux:
                        if 'A' <= letter <= 'Z':
                            letter_aux = letter
                    cuv = aux.replace(letter, cuv)
                    print(cuv)



word()