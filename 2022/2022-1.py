file = open("2022/data/2022-1.txt")
lines = file.readlines()
lutin=0
i=1
lutins=[]
max=0
for line in lines:
	value = line[:-1]
	if value == "":
		lutins.append(lutin)
		if lutin > max:
			max=lutin
			print("{} {}".format( str(i),max))
		i+=1
		lutin=0
	else:
		lutin+=int(value)


print(str(lutins))
lutins_s=lutins.sort()
print(str(lutins_s))
print(sum(lutins[-3:]))
