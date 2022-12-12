file_test = open("2022/data/2022-12-test.txt")
lines_test = file_test.readlines()
file = open("2022/data/2022-12.txt")
lines = file.readlines()
import copy

def find_path(lines):
    map = [[i for i in line.strip('\n')] for line in lines]
 
    # find S
    S = None
    E = None
    positions=[]
    for line in range(len(map)):
        for col in range(len(map[line])):
            if map[line][col] == 'S':
                S = (line, col)
                map[line][col] = 'a'
 
            if map[line][col] == 'E':
                E = (line, col)
                map[line][col] = 'z'
            
 
    print("S={}".format(S))
    print("E={}".format(E))
    #path = look_for_E([], [], S, E, map)
    d = loof_for_E_2((S[0],S[1],0),[], set(), E,map)[2]
    print("Resultat : {}".format(d))
    return d

def loof_for_E_2(position, positions, forbidden, E,map):

    if (position[0],position[1]) == E:
        return position

    if (position[0],position[1]) in forbidden:
        return loof_for_E_2(positions[0],positions[1:],forbidden,E,map)
    
    forbidden.add((position[0],position[1]))
    next_positions = [
            (position[0]+1, position[1],position[2]+1),
            (position[0], position[1]+1,position[2]+1),
            (position[0]-1, position[1],position[2]+1),
            (position[0], position[1]-1,position[2]+1),
    ]

    current_height=map[position[0]][position[1]]

    next_positions = [ pos for pos in next_positions if (
        pos[0] >= 0 and pos[0] < len(map))
        and (pos[1] >= 0 and pos[1] < len(map[0])
        and(ord(map[pos[0]][pos[1]]) - ord(current_height) <= 1))
        and (pos[0],pos[1]) not in forbidden
        ]

    positions = positions + next_positions
    return loof_for_E_2(positions[0],positions[1:],forbidden,E,map)
 
import sys
sys.setrecursionlimit(10000)
print("TEST  31 = {}".format(find_path(lines_test)))
print("PUZZLE 1 = {}".format(find_path(lines)))

def find_path_2(lines):
    map = [[i for i in line.strip('\n')] for line in lines]
 
    # find S
    S = None
    E = None
    positions=[]
    for line in range(len(map)):
        for col in range(len(map[line])):
            if map[line][col] == 'S':
                S = (line, col)
                map[line][col] = 'a'
                positions.append((line,col,1))
 
            if map[line][col] == 'E':
                E = (line, col)
                map[line][col] = 'z'
            if map[line][col] =='a':
                positions.append((line,col,1))
            
 
    print("S={}".format(S))
    print("E={}".format(E))
    #path = look_for_E([], [], S, E, map)

    d = loof_for_E_2(positions[0],positions[1:], set(), E,map)[2]
    print("Resultat : {}".format(d))
    return d - 1

print(" TEST 2 29 = {}".format(find_path_2(lines_test)))
print("PUZZLE = {}".format(find_path_2(lines)))
