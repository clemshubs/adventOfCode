
def find_galaxies(lines):
    galaxies=[]
    lines_n = set(range(0,len(lines)))
    cols_n = set(range(0,len(lines[0])))
    used_lines=set()
    used_cols=set()
    for i in range(0,len(lines)):
        if '#' in lines[i]:
            for j in range(0,len(lines[i])):
                if lines[i][j] == '#':
                    galaxies.append((i,j))
                    used_cols.add(j)
            used_lines.add(i)
    
    unused_cols = cols_n.difference(used_cols)
    unused_lines = lines_n.difference(used_lines)

    
    return galaxies, unused_lines, unused_cols

def expand_universe(lines ,unused_lines, unused_cols,expansion_rate):

    universe = []
    lines_number =len(lines)+len(unused_lines)*(expansion_rate-1)
    cols_number = len(lines[0])+len(unused_cols)*(expansion_rate-1)
    for i in range(0,len(lines)):
        if i in unused_lines:
            for _ in range(0,expansion_rate):
                universe.append(['.']*cols_number)
            
        else:
            new_line=[]

            for j in range(0,len(lines[0])):
                if j in unused_cols:
                    for _ in range(0,expansion_rate):
                        new_line.append('.')
                else:
                    new_line.append(lines[i][j])

            universe.append(new_line)

    if lines_number == len(universe):
        print("YES")
    else:
        print("NO")
    return universe

def length_of_path(gal1,gal2,unsused_lines,unsused_cols,expansion_rate):
    lines = set(range(min(gal2[0],gal1[0])+1,max(gal2[0],gal1[0])))

    lines_num_to_add = len(lines.intersection(unsused_lines))

    cols = set(range(min(gal2[1],gal1[1]),max(gal2[1],gal1[1])))
    cols_num_to_add = len(cols.intersection(unsused_cols))

    return abs(gal2[0]-gal1[0])+abs(gal2[1]-gal1[1])+cols_num_to_add*(expansion_rate-1)+lines_num_to_add*(expansion_rate-1)

def problem1(lines,expansion_rate):

    galaxies,b,c = find_galaxies(lines)
    #universe = expand_universe(lines,b,c,expansion_rate)
    #galaxies,_,_ = find_galaxies(universe)
    lengths=[]
    i=1
    for galaxy in galaxies:
        for gal2 in galaxies[i:]:
            lengths.append(length_of_path(galaxy,gal2,b,c,expansion_rate))
        i+=1
        if i == len(galaxies): 
            return sum(lengths)

# TU aoc
test1 = "...#......;\
.......#..;\
#.........;\
..........;\
......#...;\
.#........;\
.........#;\
..........;\
.......#..;\
#...#....."

file = open("2023/data/2023-11.txt")
lines = file.readlines()

galaxies,b,c = find_galaxies(test1.split(';'))

print("TU1 9 = "+str(length_of_path((6,1),(11,5),b,c,2)))
print("TU1 15 = "+str(length_of_path((0,4),(10,9),b,c,2)))
print("TU1 17 = "+str(length_of_path((2,0),(7,12),b,c,2)))
print("TU1 5 = "+str(length_of_path((11,0),(11,5),b,c,2)))
print("TU1 374 ="+str(problem1(test1.split(';'),2)))
print("PB1 9623138 ="+str(problem1(lines,2)))
print("PB2 9623138 ="+str(problem1(lines,1000000)))

