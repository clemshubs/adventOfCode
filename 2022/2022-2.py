file = open("2022/data/2022-2.txt")
lines = file.readlines()
line_n=0
score=0
for line in lines:
    value = line.strip("\n")[0]
    value_2 = line.strip("\n")[2]
    if value_2 == "X":
        score+=0
        if value == "A":
            score+=3

        if value == "B":
            score+=1   

        if value == "C":
            score+=2
    if value_2 == "Y":
        score+=3
        if value == "A":
            score+=1

        if value == "B":
            score+=2   

        if value == "C":
            score+=3
    
    if value_2 == "Z":
        score+=6
        if value == "A":
            score+=2

        if value == "B":
            score+=3   

        if value == "C":
            score+=1
    
    line_n+=1

print(score)