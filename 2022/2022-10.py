

file_test = open("2022/data/2022-10-test.txt")
lines_test = file_test.readlines()
file = open("2022/data/2022-10.txt")
lines = file.readlines()

def signal(lines):
    reg=1
    cycle=1
    scores=[0]

    for line in lines:
        op = line.split(' ')[0].strip('\n')
        if op == "noop":
            scores.append(reg)
            cycle+=1

        else:
            value = line.split(' ')[1]
            value = int(value)

            scores.append(reg)
            scores.append(reg)
            reg += value

            cycle+=2


    return scores

def result_1(scores,numbers):
    score=0
    for i in numbers:
        score+=scores[i]*i
    return score

def result_2(scores):
    scores[0]=0
    CRT=[' ' for i in range(240)]
    sprite=[0,1,2]
    crt=0
    prev=1
    for cycle in range(1,len(scores)):
        # si le score est dans le sprite, on affiche
        if crt%40 in sprite: 
            CRT[crt] = "#"
        else:
            CRT[crt] = " "

        if scores[cycle-1] != scores[cycle]:
            #fin d'addition
            sprite=[i for i in range(scores[cycle],scores[cycle]+3)]
        crt+=1

        for line in range(6):
            print("".join(CRT[line*40:(line+1)*40]))
        print("----------------------------------------")

cycles = [20,60,100,140,180,220]
print("PART 1 TEST  : 13140 =? {}".format(result_1(signal(lines_test),cycles)))
print("PART 1 PUZZLE: {}".format(result_1(signal(lines),cycles)))

print("PART 2 TEST  : {}".format(result_2(signal(lines_test))))
# en vrai, ça donne pas la bonne répone mais close enough
print("PART 2 PUZZLE: {}".format(result_2(signal(lines))))