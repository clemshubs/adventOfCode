

def first_problem(lines):
    calibration_total=0    
    for line in lines:
        first_digit=None
        last_digit=0
        for char in line:
            if char.isdigit():
                if first_digit == None:
                    first_digit=char
                last_digit=char
        if first_digit == None:
            first_digit = last_digit
        #print("CAL LIGNE " + first_digit + last_digit)
        calibration_total += int(first_digit + last_digit)


    return calibration_total

def second_probleme(lines):
    calibration_total=0

    numbers = {"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9
    ,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9}

    for line in lines:
        first_digit=("zero",-1)
        last_digit=('ten',-1)
        for number in numbers.keys():
            index = line.find(number)
            if index != -1:
                if first_digit[1] == -1:
                    first_digit = (numbers[number],index)
                else:
                    if index < first_digit[1]:
                        first_digit = (numbers[number],index)

            index = line.rfind(number)
            if index != -1:
                if last_digit[1] == -1:
                    last_digit = (numbers[number],index)
                else:
                    if index > last_digit[1]:
                        last_digit = (numbers[number],index)
        #print("CAL LIGNE " + str(first_digit[0]) + str(last_digit[0]))
        calibration_total += int(first_digit[0]*10 + last_digit[0])


    return calibration_total

test1="1abc2,pqr3stu8vwx,a1b2c3d4e5f,treb7uchet"
test2="two1nine,eightwothree,abcone2threexyz,xtwone3four,4nineeightseven2,zoneight234,7pqrstsixteen"
file = open("2023/data/2023-1.txt")
lines = file.readlines()


print("TEST1 "+ str(142 == first_problem(test1.split(','))))
print("TEST2 "+ str(281 == second_probleme(test2.split(','))))

print("TOTAL1="+str(first_problem(lines)))
print("TOTAL2="+str(second_probleme(lines)))