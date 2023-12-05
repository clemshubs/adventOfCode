def first_problem(lines):
    # cherchons les symboles
    symboles={}
    line_n=0
    for line in lines:
        char_n=0
        for char in line.strip():
            if char != '.' and not char.isdigit():
                symboles[(line_n,char_n)]=(char,[])
            char_n+=1
        line_n+=1
    
    line_n=0
    numbers=0
    for line in lines:
        char_n=0
        current_number=""
        for char in line:
            # on cherche le nombre
            if char.isdigit():
                current_number+=char
            else:
                #si c'est plus un nombre, alors on regarde autour du nombre
                if current_number.isnumeric():
                    number_kept=False
                    for line_tmp in range(max(0,line_n-1),min(line_n+1,len(lines))+1):
                        for col_tmp in range(max(0,char_n-len(current_number)-1),min(char_n+1,len(line))):
                            if (line_tmp,col_tmp) in symboles:
                                #print(current_number)
                                symboles[(line_tmp,col_tmp)]=(symboles[(line_tmp,col_tmp)][0],symboles[(line_tmp,col_tmp)][1]+[current_number])
                                numbers+=int(current_number)
                                number_kept=True
                                break
                        if number_kept:
                            break

                    current_number=""
                else:
                    #not a number.
                    pass
            char_n+=1
        line_n+=1

    #part deux
    gear_ratios=0
    for symbole in symboles.values():
        if symbole[0]=="*" and len(symbole[1]) == 2:
            gear_ratios+=int(symbole[1][0])*int(symbole[1][1])
    return numbers, gear_ratios

test1="\
467..114..;\
...*......;\
..35..633.;\
......#...;\
617*......;\
.....+.58.;\
..592.....;\
......755.;\
...$.*....;\
.664.598.."
test_bis="\
******;\
*....*;\
*.12.*;\
*....*;\
******"
test2=""
file = open("2023-3.txt")
lines = file.readlines()

print("TEST1 4361   == "+ str(first_problem(test1.split(';'))[0]))
print("TESTA 0      == "+ str(first_problem(test_bis.split(';'))[0]))
print("TEST2 467835 == "+ str(first_problem(test1.split(';'))[1]))

print("TOTAL1 546563   ="+str(first_problem(lines)[0]))
print("TOTAL2 91031374 ="+str(first_problem(lines)[1]))