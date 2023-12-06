import re
def first_problem(lines):
    
    times = re.findall(r"\d+",lines[0])
    distances = re.findall(r"\d+",lines[1])
    print(times)
    print(distances)
    solution = 1
    for i in range(0,len(times)):
        solution*=compute_solutions(times[i],distances[i])
    return solution

def compute_solutions(time, distance):
    speed_per_second = 1
    distances=[]
    for duree in range(1,int(time)+1):
        distances.append(speed_per_second*duree*(int(time)-int(duree)))
    return len([d for d in distances if d > int(distance)])

test1="\
Time:      7  15   30;\
Distance:  9  40  200"



test2=""
file = open("2023/data/2023-6.txt")
lines = file.readlines()

print("UTEST 7  9   = 4 <> " + str(compute_solutions(7,9)))
print("UTEST 15 40  = 8 <> " + str(compute_solutions(15,40)))
print("UTEST 30 200 = 9 <> " + str(compute_solutions(30,200)))
print("TEST1 288   == "+ str(first_problem(test1.split(';'))))

#print("TEST2 46   == "+ str(first_problem(test1.split(';'))[1]))


print("TOTAL1 512295 ="+str(first_problem(lines)))
#print("TOTAL2 ??? ="+str(first_problem(lines)[1]))