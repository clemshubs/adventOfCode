import re
def first_problem(lines):
    # cherchons les symboles
    final_score=0
    cards={}
    line_n=0
    #(score, nombre de cartes)
    cards[0]=(0,0)
    

    for line in lines:
        line_n+=1
        score_of_line=0
        tmp=line.split(':')[1].split('|')[0]
        winning_numbers=re.findall(r"\d+",tmp)
        
        draw_numbers=re.findall(r"\d+",line.split(':')[1].split('|')[1])
        numbers_won=0
        if line_n not in cards:
            cards[line_n]=(0,1)
        else:
            cards[line_n]=(cards[line_n][0],cards[line_n][1]+1)
        for win in winning_numbers:
            numbers_won+=1
            if win in draw_numbers:
                if score_of_line == 0:
                    score_of_line=1
                else:
                    score_of_line*=2
                cards[line_n] = (cards[line_n][0]+1 , cards[line_n][1])
        #si on a gagné
        #print("line {}".format(line_n)) 
        #print(cards)
        if score_of_line != 0:
            for i in range(line_n+1,min(len(lines)+1,line_n+cards[line_n][0]+1)):
                if i not in cards and cards[line_n]:
                    cards[i]=(0,cards[line_n][1])
                else:
                    cards[i]= (cards[i][0] , cards[i][1]+cards[line_n][1])
        #print(cards)

        final_score+=score_of_line
    

    return final_score,sum([cards[card][1] for card in cards])

test1="\
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53;\
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19;\
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1;\
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83;\
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36;\
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"

test2=""
file = open("2023/data/2023-4.txt")
lines = file.readlines()

print("TEST1 13   == "+ str(first_problem(test1.split(';'))[0]))
print("TEST2 30   == "+ str(first_problem(test1.split(';'))[1]))


print("TOTAL1 22193   ="+str(first_problem(lines)[0]))
print("TOTAL2 ??? ="+str(first_problem(lines)[1]))