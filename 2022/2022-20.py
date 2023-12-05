file_test = open("2022/data/2022-20-test.txt")
lines_test = file_test.readlines()
file = open("2022/data/2022-20.txt")
lines = file.readlines()
def build_array(lines):
    return [int(i) for i in lines]

def move_around(items):
    length=len(items)
    import copy
    items_new=copy.deepcopy(items)
    for i in items:
        if items_new.index(i)+i < length:
            
            if items_new.index(i)+i == 0:
                items_new.insert(length-1,items_new.pop(items_new.index(i)))
            else:
                items_new.insert((items_new.index(i)+i),items_new.pop(items_new.index(i)))
        else:
            items_new.insert((items_new.index(i)+i)-length+1,items_new.pop(items_new.index(i)))

    index_0=items.index(0)-1
    return items_new[(index_0+ 1000)%length]+items_new[(index_0+2000)%length]+items_new[(index_0+3000)%length]

print("TEST 3 = {}".format(move_around(build_array(lines_test))))
print("PUZZLE 3 = {}".format(move_around(build_array(lines))))
