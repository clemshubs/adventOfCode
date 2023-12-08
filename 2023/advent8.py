import re
start = "AAA"
end = "ZZZ"
import utils

def read_map(lines):
    directions = lines[0].strip()
    map = {}
    for i in range(2, len(lines)):
        node = re.findall(r'\w\w\w', lines[i].strip())
        map[node[0]] = (node[1], node[2])
    return map, directions


def navigate(map, current, end, steps, directions):
    while current != end:
        step_in_directions = steps % len(directions)
        what_to_do = directions[step_in_directions]
        if what_to_do == 'L':
            current = map[current][0]
            steps += 1
        else:
            current = map[current][1]
            steps += 1

    return steps


def navigate2(map, current, end, directions):
    # on va se souvenir de la longueur de bouclage puis calculer le ppcm
    while len([node for node in current if node[0][2] == 'Z']) != len(end):
        tmp = []

        for node in current:
            # si on a pas fini le bouclage
            if node[0][2] != 'Z':
                step_in_directions = node[1] % len(directions)
                what_to_do = directions[step_in_directions]
                if what_to_do == 'L':
                    tmp.append((map[node[0]][0], node[1] + 1))

                else:
                    tmp.append((map[node[0]][1], node[1] + 1))
            else:
                tmp.append(node)
           
        current=tmp
    
    return utils.ppcm(*[node[1] for node in current])


def problem(lines):
    map, directions = read_map(lines)
    return navigate(map, start, end, 0, directions)


def problem2(lines):
    map, directions = read_map(lines)
    start_list = [(node, 0) for node in map.keys() if node[2] == 'A']
    end_list = [node for node in map.keys() if node[2] == 'Z']
    return navigate2(map, start_list, end_list, directions)


# TU aoc
test1 = "RL;\
;\
AAA = (BBB, CCC);\
BBB = (DDD, EEE);\
CCC = (ZZZ, GGG);\
DDD = (DDD, DDD);\
EEE = (EEE, EEE);\
GGG = (GGG, GGG);\
ZZZ = (ZZZ, ZZZ)"

# autre test trouve sur reddit, mais mon erreur était ailleurs...
test2 = "LLR;\
;\
AAA = (BBB, BBB);\
BBB = (AAA, ZZZ);\
ZZZ = (ZZZ, ZZZ)"

test3 = "LR;\
;\
11A = (11B, XXX);\
11B = (XXX, 11Z);\
11Z = (11B, XXX);\
22A = (22B, XXX);\
22B = (22C, 22C);\
22C = (22Z, 22Z);\
22Z = (22B, 22B);\
XXX = (XXX, XXX)"

file = open("2023/data/2023-8.txt")
lines = file.readlines()

print("TEST1 2              = " + str(problem(test1.split(';'))))
print("TEST2 6              = " + str(problem(test2.split(';'))))

print("PROB1 22411          = "+str(problem(lines)))
print("TEST2 6              = " + str(problem2(test3.split(';'))))
print("PROB1 11188774513823 = "+str(problem2(lines)))
