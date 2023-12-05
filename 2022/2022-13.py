file_test = open("2022/data/2022-13-test.txt")
lines_test = file_test.readlines()
file = open("2022/data/2022-13.txt")
lines = file.readlines()

def compare(sum,line1,line2):
    



    return 0

def loop_on_lines(lines,compare):
    sum=0
    for i in range(0,len(lines),3):
        sum+=compare(0,lines[i],lines[i+1])