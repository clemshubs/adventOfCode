file = open("2021/data/2021-11.txt")
lines = file.readlines()
file_test = open("2021/data/2021-11-test.txt")
lines_test = file_test.readlines()

def flashing(lines,steps):
    octopussies = [[int(i) for i in line.strip('\n')] for line in lines]
    flashes=0
    for step in range(steps):
        octopussies = [[i+1 for i in line] for line in octopussies]
        flashing=True
        while flashing:
            flashing=False
            for l in range(len(octopussies)):
                for c in range(len(octopussies[l])):
                    if octopussies[l][c] >= 9:
                        flashes+=1
                        flashing=True
                        
                        try:
                            if octopussies[l-1][c-1] <= 9:
                                octopussies[l-1][c-1] +=1
                        except IndexError:
                            pass
                        try:
                            if octopussies[l-1][c] <= 9:
                                octopussies[l-1][c] +=1
                        except IndexError:
                            pass
                        try:
                            if octopussies[l-1][c+1] <= 9:
                                octopussies[l-1][c+1] +=1
                        except IndexError:
                            pass
                        try:     
                            if octopussies[l][c-1] <= 9:
                                octopussies[l][c-1] +=1
                        except IndexError:
                            pass
                        try:
                            if octopussies[l][c+1] <= 9:
                                octopussies[l][c+1] +=1
                        except IndexError:
                            pass
                        try:
                            if octopussies[l+1][c-1] <= 9:
                                octopussies[l+1][c-1] +=1
                        except IndexError:
                            pass
                        try:
                            if octopussies[l+1][c] <= 9:
                                octopussies[l+1][c] +=1
                        except IndexError:
                            pass
                        try:
                            if octopussies[l+1][c+1] <= 9:
                                octopussies[l+1][c+1] +=1    
                        except IndexError:
                            pass
                      
            octopussies = [[i if i<= 9 else 0 for i in line  ] for line in octopussies]

        #print_o(octopussies)
        #print("-------------")
    return flashes


def print_o(octo):
    for line in octo:

        print("".join([str(i) for i in line]))




print("PART 1 TEST  : 1656 =? {}".format(flashing(lines_test,100)))
print("PART 1 PUZZLE: {}".format(flashing(lines,100)))

def flashing_2(lines,steps):
    return "WIP"

print("PART 2 TEST  : 12 =? {}".format(flashing_2(lines_test,100)))
print("PART 2 PUZZLE: {}".format(flashing_2(lines,100)))
