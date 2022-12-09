file = open("2022/data/2022-4.txt")
lines = file.readlines()
line_n=0
score=0
scores = []


for line in lines:
    elfe_1,elfe_2 = line.strip('\n').split(',')
    start_1,end_1 = elfe_1.split('-')
    start_2,end_2 = elfe_2.split('-')

    # si elfe 1 comprend elfe 2
    if (int(start_1) <= int(start_2) and int(end_2) <= int(end_1)):
        print("elfe 1 contient elfe 2 : "+ str(elfe_1)+","+str(elfe_2))

        score +=1
    elif (int(start_2) <= int(start_1) and int(end_1) <= int(end_2)):
        print("elfe 2 continet elfe 1 : "+str(elfe_1)+","+str(elfe_2))
        score+=1
    
    # si elfe 2 comprend elfe 1



score2 = 0
for line in lines:
    elfe_1,elfe_2 = line.strip('\n').split(',')
    start_1,end_1 = elfe_1.split('-')
    start_2,end_2 = elfe_2.split('-')

    # pas d'over lap
    if int(end_1) < int(start_2) or int(end_2) <int(start_1) :
        print("elfe 1 n'overlap pas elfe 2 : "+ str(elfe_1)+","+str(elfe_2))

        score2 +=1
    

print("PART 1 PUZZLE  : {}".format(score))

print("PART 2 PUZZLE  : {}".format(1000 - score2))