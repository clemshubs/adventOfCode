file = open("2022/data/2022-6.txt")
lines = file.readlines()

example_1='bvwbjplbgvbhsrlpgdmjqwftvncz' #5
example_2='nppdvjthqldpwncqszvftbrmjlhg' #6
example_3='nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg' #10
example_4='zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw' #11

def find_firstchar(line,n):
	for i in range (0,len(line)-n):
		myset = set(line[i:i+n])
		if len(myset) == n:
			return i+n

print("PART 1 EXAMPLE : {} == {}".format(5,find_firstchar(example_1,4)))
print("PART 1 EXAMPLE : {} == {}".format(6,find_firstchar(example_2,4)))
print("PART 1 EXAMPLE : {} == {}".format(10,find_firstchar(example_3,4)))
print("PART 1 EXAMPLE : {} == {}".format(11,find_firstchar(example_4,4)))
print("PART 1 PUZZLE  : {}".format(find_firstchar(lines[0],4)))
print("PART 2 EXAMPLE : {} == {}".format(19,find_firstchar('mjqjpqmgbljsphdztnvjfqwrcgsmlb',14)))
print("PART 2 EXAMPLE : {} == {}".format(23, find_firstchar('bvwbjplbgvbhsrlpgdmjqwftvncz',14)))

print("PART 2 PUZZLE  : {}".format(find_firstchar(lines[0],14)))


