test1="rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"

def compute(lines):
    total_score=0
    for line in lines[0].split(','):
        score=0
        score = hash_line(line, score)
        total_score+=score

    return total_score

def hash_line(line, score):
    for a_char in line:
        score+=ord(a_char)
        score*=17
        score=score%256
    return score

def compute2(lines):
    boxes=[[] for i in range(0,256)]
    for line in lines.split(','):
        if '=' in line:
            found=False
            name,_ = line.split("=")
            box_index = hash_line(name,0)
            
            for lens in boxes[box_index]:
                if name in lens:
                    found=True
                    i = boxes[box_index].index(lens)
                    boxes[box_index][i] = line
                    break
            if not found:
                boxes[box_index].append(line)

        if '-' in line:
            name,_=line.split('-')
            box_index = hash_line(name,0)
            
            for lens in boxes[box_index]:
                if name in lens:
                    boxes[box_index].remove(lens)
                    break

    total=0
    i=0
    for box in boxes:
        j=0
        i+=1
        for lens in box:
            j+=1
            total+=( i*j * int(lens.split('=')[1]))

    return total



print(" 52 = "+str(compute("HASH")))
print(" 1320 = "+str(compute(test1)))
file = open("2023/data/2023-15.txt")
lines=file.readlines()

print(" .... = "+str(compute(lines)))

print(" 145 = "+str(compute2(test1)))
print(" ?? = "+str(compute2(lines[0])))