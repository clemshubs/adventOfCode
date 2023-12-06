def first_problem(lines,max_red,max_blue,max_green):
    sum_id=0
    for line in lines:
        colors={"red":0,"blue":0,"green":0}
        
        game_number = int(line.split(':')[0].split(' ')[1])
        game=line.split(':')[1]
        runs=game.split(';')
        game_impossible=False
        for run in runs:
            draws=run.split(',')
            for draw in draws:
                color = draw.split(' ')[2].strip()
                colors[color]=int(draw.split(' ')[1])


            if colors["red"] > max_red or colors["blue"] > max_blue or colors["green"] > max_green:
                game_impossible=True
                break
        
        
        if not game_impossible:
            sum_id += game_number
        

    return sum_id

def second_probleme(lines):
    sum_id=0
    for line in lines:
        colors={"red":0,"blue":0,"green":0}        
        game=line.split(':')[1]
        runs=game.split(';')
        game_power=1
        min_red=None
        min_blue=None
        min_green=None
        for run in runs:
            draws=run.split(',')
            for draw in draws:
                color = draw.split(' ')[2].strip()
                colors[color]=int(draw.split(' ')[1])
                if color == "red" and min_red==None:
                    min_red=colors[color]
                if color == "blue" and min_blue==None:
                    min_blue=colors[color]
                if color == "green" and min_green==None:
                    min_green=colors[color]

            if min_red != None and colors["red"] > min_red :
                min_red=colors["red"]
               
            if min_blue != None and colors["blue"] > min_blue :
                min_blue=colors["blue"]
                
            if min_green != None and colors["green"] > min_green :
                min_green=colors["green"] 
        

        game_power = min_red*min_blue*min_green
        #print(str(game_power)+" "+str(min_red)+" "+str(min_blue)+" "+str(min_green))
        sum_id += game_power

    return sum_id

test1="Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green!Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue!Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red!Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red!Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"
test2=""
file = open("2023/data/2023-2.txt")
lines = file.readlines()

print("TEST1 8 == "+ str(first_problem(test1.split('!'),12,14,13)))
print("TEST 2286 "+ str(second_probleme(test1.split('!'))))

print("TOTAL1="+str(first_problem(lines,12,14,13)))
print("TOTAL2="+str(second_probleme(lines)))