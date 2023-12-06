import re
def first_problem(lines):
    lowest_seed=0
    tables=[]
    current_table=None
    seeds=[]
    for line in lines:
        if line == "":
            continue
        else: 
            if not line[0].isnumeric():
                if "seeds" in line:
                    seeds=re.findall(r"\d+",line)
                    continue
                else:
                    if current_table != None:
                        tables.append(current_table)
                    current_table={"name":line, "conversions":[]}
            else:
                current_table["conversions"].append([int(item) for item in re.findall(r"\d+",line)])
        
    tables.append(current_table)
    # toutes mes tables sont OK.
    #Maintenant, faut convertir.
    def from_to(number_in,table,tables):
        
        number_out=number_in
        for conversion in table["conversions"]:
            if conversion[1] <= number_in and number_in < conversion[1] + conversion[2]:
                number_out=number_in+conversion[0]-conversion[1]
                break
        if len(tables)==0:
            return number_out
        else:  
            return from_to(number_out,tables[0],tables[1:])
    
    #une range, c'est debut, duree, delta

    #on va precalculer toutes les sous ranges avec leur delta par rapport à N
    def precompute_ranges(ranges,table,tables):
        new_ranges=set()
        # initialiser les ranges avec la premiere table
        if len(ranges)==0:
            for conversion in table["conversions"]:
                new_ranges.add((conversion[1],conversion[1] + conversion[2]-1,conversion[0]-conversion[1]))
        else:
            #je vais les appliquer à mes ranges
            for a_range in ranges:
                for conversion in table["conversions"]:
                    new_ranges.update(apply_conversion_to_range(a_range,conversion))
        print(table["name"]+ "="+ str(len(new_ranges)))
        print(sorted(new_ranges))       

        if len(tables)==0:
            return new_ranges
        else:
            return precompute_ranges(new_ranges,tables[0],tables[1:])

    def apply_conversion_to_range(in_range,conversion):
        # (debut, fin, delta)
        # (conversion[1],conversion[1] + conversion[2],conversion[0]-conversion[1])
        #si on a une intersection        
        conversion_range=(conversion[1],conversion[1] + conversion[2]-1,conversion[0]-conversion[1])

        #on applique la transformation courante
        a_range=(in_range[0]+in_range[2],in_range[1]+in_range[2],in_range[2])

        # si c'est exclus, on fait rien et on retourne les deux ranges
        if  conversion_range[1] < a_range[0] or a_range[1] < conversion_range[0]:
            return []
        
        # sinon, faut faire dékalkul
        else:
            # si c'est inclus
            if conversion_range[0] <= a_range[0] <= conversion_range[1] and conversion_range[0] <= a_range[1] <= conversion_range[1]:
                return [
                (in_range[0],in_range[1],conversion_range[2]+in_range[2])
                ]
            #alors c'est compris
            elif a_range[0] <= conversion_range[0]  and conversion_range[1] <= a_range[1]:
                return [
                (in_range[0],conversion_range[0]-in_range[2],in_range[2]),
                (conversion_range[0]-in_range[2]+1,conversion_range[1]-in_range[2],conversion_range[2]+in_range[2]),
                (conversion_range[1]-in_range[2]+1,in_range[1],in_range[2])
                ]

            #si c'est a gauche
            elif  a_range[0] <= conversion_range[0]   and conversion_range[0] <= a_range[1] <= conversion_range[1]:
                return [
                (in_range[0] , conversion_range[0]-in_range[2]-1 , in_range[2]),
                (conversion_range[0]-in_range[2],in_range[1],in_range[2] + conversion_range[2])
                ]
            #si c'est a droite
            elif conversion_range[0] <= a_range[0] <= conversion_range[1]  and conversion_range[1] <= a_range[1]:
                return [
                (in_range[0],conversion_range[1] - in_range[2] , in_range[2] + conversion_range[2]),
                (conversion_range[1] - in_range[2] +1 , in_range[1], a_range[2] )
                ]
            else:
                print("panapan")
            
    print(precompute_ranges([],tables[0],tables[1:]))
    min1=min([from_to(int(seed),tables[0],tables[1:]) for seed in seeds])
    print(min1)
    
    seeds2=[]
    min2=None

    for i in range(0,len(seeds),2):
        for seed in range(int(seeds[i]),int(seeds[i])+ int(seeds[i+1])):
            seed_out = from_to(seed,tables[0],tables[1:])
            if min2 == None:
                min2=seed_out
            if seed_out < min2:
                min2=seed_out
            

    return min1,min2

test1="seeds: 79 14 55 13;\
;\
seed-to-soil map:;\
50 98 2;\
52 50 48;\
;\
soil-to-fertilizer map:;\
0 15 37;\
37 52 2;\
39 0 15;\
;\
fertilizer-to-water map:;\
49 53 8;\
0 11 42;\
42 0 7;\
57 7 4;\
;\
water-to-light map:;\
88 18 7;\
18 25 70;\
;\
light-to-temperature map:;\
45 77 23;\
81 45 19;\
68 64 13;\
;\
temperature-to-humidity map:;\
0 69 1;\
1 0 69;\
;\
humidity-to-location map:;\
60 56 3;\
56 93 4;"

test2=""
file = open("2023/data/2023-5.txt")
lines = file.readlines()

print("TEST1 35   == "+ str(first_problem(test1.split(';'))[0]))
print("TEST2 46   == "+ str(first_problem(test1.split(';'))[1]))


print("TOTAL1 313045984   ="+str(first_problem(lines)[0]))
print("TOTAL2 ??? ="+str(first_problem(lines)[1]))