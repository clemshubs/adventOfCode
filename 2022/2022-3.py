file = open("2022/data/2022-3.txt")
lines = file.readlines()
line_n=0
score=0
scores = []
alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
for line in lines:
    value = line.strip("\n")
    cut = int(len(value)/2)
    value_1 = value[0:cut]
    value_2 = value[cut:]
    intersect = [ a for a in value_1 if a in value_2]
    score += alpha.index(intersect[0]) + 1
    line_n+=1

print("PART 1 PUZZLE : {}".format(score))
score = 0
    
for i in range(0,len(lines),3):
    intersect = []
    value_1=lines[i].strip("\n")
    value_2=lines[i+1].strip("\n")
    value_3=lines[i+2].strip("\n")
    intersect = [ a for a in value_1 if a in value_2]
    intersect = [ a for a in intersect if a in value_3]
    score += alpha.index(intersect[0]) + 1
print("PART 2 PUZZLE : {}".format(score))
