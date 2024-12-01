import math

def make_two_lists(lines):
# on cree les deux listes
    left=[]
    right=[]
    
    for line in lines:
        left.append(int(line.split("   ")[0]))
        right.append(int(line.split("   ")[1]))
    return left,right

def first_problem(lines):
    left,right = make_two_lists(lines)
       
    left.sort()
    right.sort()
    differences = [abs(left[i]-right[i]) for i in range(0,len(lines))]
    return sum(differences)

def second_probleme(lines):
    total = 0
    left,right = make_two_lists(lines)
    for number in left:
        total += number*right.count(number)
    return total

file = open("2024/data/2023-1.txt")
lines = file.readlines()
test1 = ["3   4",
"4   3",
"2   5",
"1   3",
"3   9",
"3   3"]
print("TEST1 "+ str(11 == first_problem(test1)))
print("TEST2 "+ str(31 == second_probleme(test1)))


print("TOTAL1="+str(first_problem(lines)))
print("TOTAL2="+str(second_probleme(lines)))