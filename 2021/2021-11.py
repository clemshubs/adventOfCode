file = open("2021/data/2021-6.txt")
lines = file.readlines()
file_test = open("2021/data/2021-6-test.txt")
lines_test = file_test.readlines()


print("PART 1 TEST  : 5 =? {}".format(overlaping_points(lines_test)))
print("PART 1 PUZZLE: {}".format(overlaping_points(lines)))



print("PART 2 TEST  : 12 =? {}".format(overlaping_points_2(lines_test)))
print("PART 2 PUZZLE: {}".format(overlaping_points_2(lines)))
