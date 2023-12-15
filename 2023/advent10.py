import re

def read_map(lines):
    start=(0,0)
    mymap={}
    for line_n in range(0,len(lines)):
        mymap[line_n]={}
        for col_n in range(0,len(lines[line_n].strip())):
            char=lines[line_n][col_n]
            if char=='S':
                start=(line_n,col_n)
            mymap[line_n][col_n]=char

    return mymap,start

def find_loop(mymap,start,previous_step,step,length):
    
    if step == start:
        return length
    elif not (0<=step[0] <len(mymap)):
        return -1
    elif not (0<=step[1] <len(mymap[0])):
        return -1
    else:
        match mymap[step[0]][step[1]]:
            case 'F':
                if previous_step == (step[0]+1,step[1]):
                    return find_loop(mymap,start,step,(step[0],step[1]+1),length+1)
                elif previous_step == (step[0],step[1]+1):
                    return find_loop(mymap,start,step,(step[0]+1,step[1]),length+1)
                else:
                    return -1
            case "7":
                if previous_step == (step[0]+1,step[1]):
                    return find_loop(mymap,start,step,(step[0],step[1]-1),length+1)
                elif previous_step == (step[0],step[1]-1):
                    return find_loop(mymap,start,step,(step[0]+1,step[1]),length+1)
                else:
                    return -1
            case "J":
                if previous_step == (step[0]-1,step[1]):
                    return find_loop(mymap,start,step,(step[0],step[1]-1),length+1)
                elif previous_step == (step[0],step[1]-1):
                    return find_loop(mymap,start,step,(step[0]-1,step[1]),length+1)
                else:
                    return -1
            case "L":
                if previous_step == (step[0]-1,step[1]):
                    return find_loop(mymap,start,step,(step[0],step[1]+1),length+1)
                elif previous_step == (step[0],step[1]+1):
                    return find_loop(mymap,start,step,(step[0]-1,step[1]),length+1)
                else:
                    return -1
            case "|":
                if previous_step == (step[0]-1,step[1]):
                    return find_loop(mymap,start,step,(step[0]+1,step[1]),length+1)
                elif previous_step == (step[0]+1,step[1]):
                    return find_loop(mymap,start,step,(step[0]-1,step[1]),length+1)
                else:
                    return -1
            case "-":
                if previous_step == (step[0],step[1]-1):
                    return find_loop(mymap,start,step,(step[0],step[1]+1),length+1)
                elif previous_step == (step[0],step[1]+1):
                    return find_loop(mymap,start,step,(step[0],step[1]-1),length+1)
                else:
                    return -1
            case _:
                return -1

def find_path(mymap,start):
    
    next_steps=[(start[0]-1,start[1]),
                (start[0],start[1]-1),
                (start[0]+1,start[1]),
                (start[0],start[1]+1)]
    
    for step in next_steps:
        length = find_loop(mymap,start,start,step,0)
    return round(length/2)
# TU aoc
test1 = "\
-L|F7;\
7S-7|;\
L|7||;\
-L-J|;\
L|-JF"

test2="7-F7-;\
.FJ|7;\
SJLL7;\
|F--J;\
LJ.LJ"
file = open("2023/data/2023-10.txt")
lines = file.readlines()
import sys
sys.setrecursionlimit(100000)

print("TU  4 = "+str(find_path(*read_map(test1.split(';')))))
print("TU  8 = "+str(find_path(*read_map(test2.split(';')))))
print("PB  ? = "+str(find_path(*read_map(lines))))
