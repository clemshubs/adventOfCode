import re
import utils



def find_next_value(line):

    intervals = [int(line[i+1])-int(line[i]) for i in range(0,len(line)-1)]
    
    if all(map(lambda x: x == 0, intervals)):
        return int(line[-1]) + intervals[-1]
    else:
        return find_next_value(intervals)+int(line[-1])
    


def find_previous_value(line):

    intervals = [int(line[i+1])-int(line[i]) for i in range(0,len(line)-1)]
    
    if all(map(lambda x: x == 0, intervals)):
        return int(line[0]) - intervals[-1]
    else:
        return int(line[0]) - find_previous_value(intervals)
    
def problem(lines):
    new_values=[find_next_value(re.findall(r'[\-]?\d+',line.strip())) for line in lines]
    return sum(new_values)

def problem2(lines):
    new_values=[find_previous_value(re.findall(r'[\-]?\d+',line.strip())) for line in lines]
    return sum(new_values)
# TU aoc
test1 = "0 3 6 9 12 15;\
1 3 6 10 15 21;\
10 13 16 21 30 45"

file = open("2023/data/2023-9.txt")
lines = file.readlines()
print("TU  1 18         = " + str(find_next_value(re.findall(r'[-]?\d+',test1.split(';')[0]))))
print("TU  1 28         = " + str(find_next_value(re.findall(r'[-]?\d+',test1.split(';')[1]))))
print("TU  1 68         = " + str(find_next_value(re.findall(r'[-]?\d+',test1.split(';')[2]))))
print("TEST1 114        = " + str(problem(test1.split(';'))))

print("PROB1 1921197370 = "+str(problem(lines)))
print("TU  2 5          = " + str(find_previous_value(re.findall(r'[-]?\d+',test1.split(';')[2]))))
print("PROB2 1124       = "+str(problem2(lines)))

