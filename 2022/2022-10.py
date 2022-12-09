

file_test = open("2022/data/2022-10-test.txt")
lines_test = file_test.readlines()
file = open("2022/data/2022-10.txt")
lines = file.readlines()
print("PART 1 TEST  : XX =? {}".format(XXX(lines_test)))
print("PART 1 PUZZLE: {}".format(XXX(lines)))


file_test_2 = open("2022/data/2022-9-test-2.txt")
lines_test_2 = file_test_2.readlines()
print("PART 2 TEST  : XX == {}".format(count_positions_rope(lines_test_2)))
print("PART 2 PUZZLE: {}".format(count_positions_rope(lines)))
