import re
from math import sqrt, trunc


def first_problem(lines):

    times = re.findall(r"\d+", lines[0])
    distances = re.findall(r"\d+", lines[1])

    solution1 = 1
    for i in range(0, len(times)):
        solution1 *= compute_solutions(int(times[i]), int(distances[i]))

    solution2 = compute_solutions(int(''.join(times)), int(''.join(distances)))
    return solution1, solution2


def compute_solutions(time, distance):
    # length < hold * (time - hold)
    # 0 < - hold^2 -time*hold - length
    # 0 < -d^2 +t -l
    a = -1
    b = -time
    c = -distance
    delta = b*b - 4*a*c

    x1 = (-b - sqrt(delta))/2*a
    x2 = (-b + sqrt(delta))/2*a

    return trunc(x1) - trunc(x2)


test1 = "\
Time:      7  15   30;\
Distance:  9  40  200"


test2 = ""
file = open("2023/data/2023-6.txt")
lines = file.readlines()

print("UTEST 7  9      = 4 <> " + str(compute_solutions(7, 9)))
print("UTEST 15 40     = 8 <> " + str(compute_solutions(15, 40)))
print("UTEST 30 200    = 9 <> " + str(compute_solutions(30, 200)))
print("TEST1 288 '     = " + str(first_problem(test1.split(';'))[0]))

print("TEST2 71503     = " + str(first_problem(test1.split(';'))[1]))


print("TOTAL1 512295   ="+str(first_problem(lines)[0]))
print("TOTAL2 36530883 ="+str(first_problem(lines)[1]))
