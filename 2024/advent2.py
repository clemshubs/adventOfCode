def is_safe_decrease(line):
# on cree les deux listes
    is_safe=True
    i=0
    for i in range(1,len(line)):
        if int(line[i-1]) >= int(line[i])  and 0 <  abs(int(line[i-1]) - int(line[i]))  < 4:
            pass
        else:
            is_safe = False
    #print("dec safe is {} for line {}".format(is_safe,line))

    return is_safe

def is_safe_increase(line):
# on cree les deux listes
    is_safe=True
    i=0
    for i in range(1,len(line)):
        if int(line[i-1]) <= int(line[i])  and 0 <  abs(int(line[i-1]) - int(line[i]))  < 4:
            pass
        else:
            is_safe = False
    
    #print("inv safe is {} for line {}".format(is_safe,line))

    return is_safe


def first_problem(lines):
    total=0
    for line in lines:
        line_s = line.split(" ")
        if is_safe_decrease(line_s) or is_safe_increase(line_s):
            total+=1
    return total

def second_probleme(lines):
    total=0
    for line in lines:
        line_s = line.split(" ")
        if is_safe_decrease(line_s) or is_safe_increase(line_s):
            total+=1
        else:
            for i in range(0,len(line_s)):
                if is_safe_decrease(line_s[0:i]+line_s[i+1:]) or is_safe_increase(line_s[0:i]+line_s[i+1:]):
                    total+=1
                    break

    return total


file = open("2024/data/2024-2.txt")
lines = file.readlines()
test1 = ["7 6 4 2 1",
"1 2 7 8 9",
"9 7 6 2 1",
"1 3 2 4 5",
"8 6 4 4 1",
"1 3 6 7 9"]

print("TEST1 "+ str( 2 == first_problem(test1)))
print("TEST2 "+ str( 4 == second_probleme(test1)))


print("TOTAL1="+str(606 == first_problem(lines)))

print("TOTAL2="+str(644 == second_probleme(lines)))