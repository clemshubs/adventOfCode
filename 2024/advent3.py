import re

def first_problem(lines):
    total=0
    p=re.compile("mul\((\d?\d?\d),(\d?\d?\d)\)")
    for line in lines:
       for result in p.findall(line):
           #print(str(result))
           total+=int(result[0])*int(result[1])
    return total

def second_probleme(lines):
    total=0
    dont=False
    p=re.compile("(do\(\))|(don't\(\))|mul\((\d?\d?\d),(\d?\d?\d)\)")
    for line in lines:
       for result in p.findall(line):
            if result[1]:
               dont=True
            elif result[0]:
               dont=False
            else:
                if not dont:
                    total+=int(result[2])*int(result[3])
    return total

file = open("2024/data/2024-3.txt")
lines = file.readlines()
test1 = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
test2="xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
print("TEST1 "+ str( 161 == first_problem([test1])))
print("TEST2 "+ str( 48 == second_probleme([test2])))


print("TOTAL1="+str(first_problem(lines)))
print("TOTAL2="+str(second_probleme(lines)))