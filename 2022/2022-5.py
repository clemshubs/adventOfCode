file = open("2022/data/2022-5.txt")
lines = file.readlines()

# find line of indexes
line_of_index=0
while lines[line_of_index][0:2] != " 1":
	line_of_index+=1

col_number = int(lines[line_of_index][-3])
print("Col number: {}".format(col_number))
line = 0
#charger les colonnes

def get_cols(lines,col_number):
	line=0
	cols=[None,[],[],[],[],[],[],[],[],[]]
	for line in lines[0:line_of_index]:
		for col in range(0,col_number):
			if line[col*4+1] != " ":
				cols[col+1].append(line[col*4+1])
	return cols

line +=2

cols=get_cols(lines,col_number)
print(cols)
for line in range(line_of_index + 2,len(lines)):
	move_x, from_x = lines[line].split('from')
	from_x ,to_x = from_x.split("to")
	move_x = int(move_x.split("move")[1][1:])
	to_x=int(to_x[1:])
	from_x=int(from_x[1:])
	
	for i in range(0,move_x):
		cols[to_x].insert(0,cols[from_x].pop(0))

print("PART 1 PUZZLE : {}".format("".join([col[0] for col in cols[1:]])))

cols=get_cols(lines,col_number)
for line in range(line_of_index+2,len(lines)):
	move_x, from_x = lines[line].split('from')
	from_x ,to_x = from_x.split("to")
	move_x = int(move_x.split("move")[1][1:])
	to_x=int(to_x[1:])
	from_x=int(from_x[1:])
	col_to_move = cols[from_x][0:move_x]
	col_remaining = cols[from_x][move_x:]
	cols[to_x] = col_to_move + cols[to_x]
	cols[from_x] = col_remaining

solution_trouvée="".join([col[0] for col in cols[1:]])

print("PART 2 PUZZLE : {}".format(solution_trouvée))
