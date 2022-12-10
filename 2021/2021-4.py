file = open("2021/data/2021-4.txt")
lines = file.readlines()
file_test = open("2021/data/2021-4-test.txt")
lines_test = file_test.readlines()

def bingo(lines):
    numbers=(int(n) for n in lines[0].split(','))
    boards=[]
    winning_boards=set()
    scores=[]
    #making boards
    for i in range(2,len(lines),6):
        boards.append(make_board(lines[i:i+5]))

    for number in numbers:
        for board in boards:
            # on coche
            for line in board:
                for i in range(len(line)):
                    if line[i] == number:
                        line[i]=" "
            # on verifie
            for line in board:
                if len(set(line)) == 1 and line[0]==" ":
                    scores.append(compute_victory(board,number))
                    winning_boards.add(boards.index(board))
                    if len(winning_boards)==len(boards):
                        return scores
            for col in range(5):
                if len(set([board[i][col] for i in range(5) ])) == 1 and board[1][col] == " ":
                    scores.append(compute_victory(board,number))
                    winning_boards.add(boards.index(board))
                    if len(winning_boards)==len(boards):
                        return scores

    return scores[0],
def compute_victory(board,number):
    score=0
    for line in board:
        for num in line:
            if num != " ":
                score+=num
    return score * number


def make_board(lines):
    ret=[]
    for line in lines:
        l=[]
        for num in line.strip('\n').replace('  ',' ').split(' '):
            if num != "":
                l.append(int(num))
        ret.append(l)
    return ret

print("PART 1 TEST  : 4512 =? {}".format(bingo(lines_test)[0]))
print("PART 1 PUZZLE: {}".format(bingo(lines)[0]))


print("PART 2 TEST  : 1924 =? {}".format(bingo(lines_test)[-1]))
print("PART 2 PUZZLE: {}".format(bingo(lines)[-1]))