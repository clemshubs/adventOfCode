import math
def possibilities(line):
    n = 0
    enigma,record = line.split(' ')
    groups = enigma.split('.')
    groups = [group for group in groups if group != '']
    records = [int(rec) for rec in record.split(',')]

    if len(groups) == len(record.split(',')):
        possibilities_per_group = 1
        for i in range(0,len(groups)):
            possibilities_per_group *=  (len(groups[i])-records[i]+1)

    

    return possibilities_per_group
def p_parmi_n(p,n):
    
    return math.factorial(n)/(math.factorial(n-p)*math.factorial(p))

# TU aoc
test1 = "???.### 1,1,3;\
.??..??...?##. 1,1,3;\
?#?#?#?#?#?#?#? 1,3,1,6;\
????.#...#... 4,1,1;\
????.######..#####. 1,6,5;\
?###???????? 3,2,1"

file = open("2023/data/2023-11.txt")
lines = file.readlines()

print("TU ligne 1 4 = "+str(possibilities(test1.split(';')[1])))