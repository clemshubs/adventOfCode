file = open("2021/data/2021-5.txt")
lines = file.readlines()
file_test = open("2021/data/2021-5-test.txt")
lines_test = file_test.readlines()

def overlaping_points(lines):
    lines_o=[]
    max_x=0
    max_y=0
    for line in lines: 
        line_o=line.split(' -> ')
        x1,y1 = line_o[0].split(',')
        x2,y2 = line_o[1].split(',')
        if x1 == x2 or int(y1) == int(y2):
            lines_o.append(((int(x1),int(y1)),(int(x2),int(y2))))
        if int(x1)>max_x:
            max_x=int(x1)
        if int(x2)>max_x:
            max_x=int(x2)
        if int(y1)>max_y:
            max_y=int(y1)
        if int(y2)>max_y:
            max_y=int(y2)

    #inti
    array=[[0 for i in range(max_y+1)] for j in range(max_x+1)]

    for line in lines_o:
        if line[0][0] == line[1][0]:
            #meme x
            x = line[0][0]
            y1=line[0][1]
            y2=line[1][1]
            for y in range(min(y1,y2),max(y1,y2)+1):
                array[x][y]+=1
        if line[0][1] == line[1][1]:
            #meme y
            x=line[0][1]
            y1=line[0][0]
            y2=line[1][0]
            for y in range(min(y1,y2),max(y1,y2)+1):
                array[y][x]+=1
    score=0
    for line in array:
        for i in line:
            if i > 1:
                score+=1
    return score
print("PART 1 TEST  : 5 =? {}".format(overlaping_points(lines_test)))
print("PART 1 PUZZLE: {}".format(overlaping_points(lines)))

def overlaping_points_2(lines):
    lines_o=[]
    max_x=0
    max_y=0
    for line in lines: 
        line_o=line.split(' -> ')
        x1,y1 = line_o[0].split(',')
        x2,y2 = line_o[1].split(',')
        x1=int(x1)
        x2=int(x2)
        y1=int(y1)
        y2=int(y2)
        if x1 == x2 or int(y1) == int(y2):
            lines_o.append(((int(x1),int(y1)),(int(x2),int(y2))))
        else:
            # diagonale qui descend
            if x1 > x2:
                for i in range(x1-x2+1):
                    if y1 > y2:
                        lines_o.append(((x1-i,y1-i),(x1-i,y1-i)))
                    else:
                        lines_o.append(((x1-i,y1+i),(x1-i,y1+i)))

            # diagonale qui monte
            else:
                for i in range(x2-x1+1):
                    if y1 > y2:
                        lines_o.append(((x1+i,y1-i),(x1+i,y1-i)))
                    else:
                        lines_o.append(((x1+i,y1+i),(x1+i,y1+i)))

        if int(x1)>max_x:
            max_x=int(x1)
        if int(x2)>max_x:
            max_x=int(x2)
        if int(y1)>max_y:
            max_y=int(y1)
        if int(y2)>max_y:
            max_y=int(y2)

    #inti
    array=[[0 for i in range(max_y+1)] for j in range(max_x+1)]

    for line in lines_o:
        if line[0][0] == line[1][0]:
            #meme x
            x = line[0][0]
            y1=line[0][1]
            y2=line[1][1]
            for y in range(min(y1,y2),max(y1,y2)+1):
                array[x][y]+=1
        elif line[0][1] == line[1][1]:
            #meme y
            x=line[0][1]
            y1=line[0][0]
            y2=line[1][0]
            for y in range(min(y1,y2),max(y1,y2)+1):
                array[y][x]+=1
    score=0
    for line in array:
        for i in line:
            if i > 1:
                score+=1
    return score
print("PART 2 TEST  : 12 =? {}".format(overlaping_points_2(lines_test)))
print("PART 2 PUZZLE: {}".format(overlaping_points_2(lines)))
