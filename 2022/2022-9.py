
def count_positions(lines):
    position_tail = (0, 0)
    position_head = (0, 0)
    tail_positions = set()
    tail_positions.add(position_tail)

    for line in lines:
        direction = line[0]
        move = int(line.split(' ')[1])

        for _ in range(move):
            position_head, movement_head = new_position_head(
                position_head, direction, 1)

            position_tail = new_position_tail(
                position_head, movement_head, position_tail)

            tail_positions.add(position_tail)


    return len(set(tail_positions))


def new_position_tail(position_head, movement_head, position_tail):
    # si a cote, on bouge pas
    if abs(position_head[0]-position_tail[0]) <= 1 and abs(position_head[1]-position_tail[1]) <= 1:
        pass            # si on monte de 1
    elif abs(position_head[0]-position_tail[0]) > 1 and position_head[1] == position_tail[1]:
        position_tail = (
            position_tail[0]+movement_head[0], position_tail[1])

    elif abs(position_head[1]-position_tail[1]) > 1 and position_head[0] == position_tail[0]:
        position_tail = (
            position_tail[0], position_tail[1]+movement_head[1])

    # si on a deux lignes de différence et une colonne de différence :
    else:
        movement_tail_ud = 0
        movement_tail_lr = 0
        if position_head[0] > position_tail[0]:
            movement_tail_ud = 1
        else:
            movement_tail_ud = -1
        if position_head[1] > position_tail[1]:
            movement_tail_lr = 1
        else:
            movement_tail_lr = -1

        position_tail = (
            position_tail[0]+movement_tail_ud, position_tail[1]+movement_tail_lr)

    return position_tail

def new_position_head(head_position, direction, move):
    if direction == 'U':
        return (head_position[0]+move, head_position[1]), (move, 0)
    if direction == 'D':
        return (head_position[0]-move, head_position[1]), (-move, 0)
    if direction == 'L':
        return (head_position[0], head_position[1]-move), (0, -move)
    if direction == 'R':
        return (head_position[0], head_position[1]+move), (0, move)


file_test = open("2022/data/2022-9-test.txt")
lines_test = file_test.readlines()
file = open("2022/data/2022-9.txt")
lines = file.readlines()
print("PART 1 TEST  : 13 =? {}".format(count_positions(lines_test)))
print("PART 1 PUZZLE: {}".format(count_positions(lines)))


# part 2


def count_positions_rope(lines):
    rope_l = 10
    # head à 0, tail à 8
    rope = [(0, 0) for i in range(rope_l)]

    tail_positions = set()
    tail_positions.add((0, 0))

    for line in lines:
        direction = line[0]
        move = int(line.split(' ')[1])

        for _ in range(move):
            rope[0], movement_head = new_position_head(
                    rope[0],direction, 1)
            for knot_n in range(1,len(rope)):
                
            #display(position_tail, position_head)
                new_knot = new_position_tail(
                    rope[knot_n-1], movement_head, rope[knot_n])
                movement_head=(new_knot[0]-rope[knot_n][0],new_knot[1]-rope[knot_n][1])
                rope[knot_n]=new_knot
            tail_positions.add(rope[-1])

    return len(set(tail_positions))

file_test_2 = open("2022/data/2022-9-test-2.txt")
lines_test_2 = file_test_2.readlines()
print("PART 2 TEST  : 36 == {}".format(count_positions_rope(lines_test_2)))
print("PART 2 PUZZLE: {}".format(count_positions_rope(lines)))
