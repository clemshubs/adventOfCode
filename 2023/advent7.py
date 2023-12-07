
cards=[ 'A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
cards2=[ 'A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']
types={
        5:7,
        4:6,
        "Full":5,
        3:4,
        "2P":3,
        2:2,
        1:1
    }

def identify_nature2(hand):
        hand_dict={}
        for card in cards:
            hand_dict[card]=hand.count(card)
        
        j_number=hand_dict.pop('J')
        numerous_cards_count=sorted(hand_dict.values())[-1]
        
        numerous_cards_count+=j_number
        
        if numerous_cards_count == 5 or numerous_cards_count == 4  or numerous_cards_count == 1:
            return types[numerous_cards_count]
        if numerous_cards_count == 3:
            if sorted(hand_dict.values())[-2] == 2 :
                return types["Full"]
            else:
                return types[3]
        if  numerous_cards_count == 2:
            if sorted(hand_dict.values())[-2] == 2 :
                return types["2P"]
            else:
                return types[2]


def identify_nature(hand):
        hand_dict=[]
        for card in cards:
            hand_dict.append(hand.count(card))
        

        numerous_cards_count=sorted(hand_dict)[-1]

        if numerous_cards_count == 5 or numerous_cards_count == 4  or numerous_cards_count == 1:
            return types[numerous_cards_count]
        if numerous_cards_count == 3:
            if sorted(hand_dict)[-2] == 2 :
                return types["Full"]
            else:
                return types[3]
        if  numerous_cards_count == 2:
            if sorted(hand_dict)[-2] == 2 :
                return types["2P"]
            else:
                return types[2]

def compare2(hand1,hand2):
    nature_h1 =  identify_nature2(hand1)
    nature_h2 =  identify_nature2(hand2)
    if nature_h1 != nature_h2:
        return nature_h1 < nature_h2
    else:
        for i in range(0,5):
            #logique inversée sur mes cartes
            card1 = cards.index(hand1[i])
            card2 = cards.index(hand2[i])
            if card1 != card2:
                return card1 > card2
    print("PASNORMAL")
    return True

def compare(hand1,hand2):
    nature_h1 =  identify_nature(hand1)
    nature_h2 =  identify_nature(hand2)
    if nature_h1 != nature_h2:
        return nature_h1 < nature_h2
    else:
        for i in range(0,5):
            #logique inversée sur mes cartes
            card1 = cards.index(hand1[i])
            card2 = cards.index(hand2[i])
            if card1 != card2:
                return card1 > card2
    print("PASNORMAL")
    return True

def first_problem(lines):
   
    
    hands= [ line.strip().split(' ') for line in lines]
    bubble_sort(hands,compare)

    solution1=0
    i=len(hands)
    for hand in bubble_sort(hands,compare):
        solution1+=i*int(hand[1])
        i-=1
    
    solution2=0
    i=len(hands)
    for hand in bubble_sort(hands,compare2):
        solution2+=i*int(hand[1])
        i-=1
    return solution1, solution2

def bubble_sort(array, compare):

    n = len(array)

    for i in range(n):

        already_sorted = True

        for j in range(n - i - 1):

            if compare(array[j][0], array[j + 1][0]):
                array[j], array[j + 1] = array[j + 1], array[j]
                already_sorted = False
        if already_sorted:

            break


    return array


test1 = "\
32T3K 765;\
T55J5 684;\
KK677 28;\
KTJJT 220;\
QQQJA 483"


test2 = ""
file = open("2023/data/2023-7.txt")
lines = file.readlines()

print("UTEST 33332 < 2AAAA = False " + str(compare("33332", "2AAAA")))
print("UTEST 77888 < 77788 = False " + str(compare("77888", "77788")))
print("UTEST JJJTT < Q2226 = False " + str(compare("JJJTT", "JQAQQ")))

print("UTEST nature of JJTTT= FULL 7" + str(identify_nature2("JJJTT")))
print("UTEST nature of QJJQ2=    4 6" + str(identify_nature2("QJJQ2")))
print("UTEST JKKK2 < QQQQ2 = True " + str(compare2("JKKK2", "QQQQ2")))

res = first_problem(test1.split(';'))
print("TEST1 6440 '     = " + str(res[0]))

print("TEST2 5905     = " + str(res[1]))

res = first_problem(lines)
print("TOTAL1 253603890   = "+str(res[0]))
print("TOTAL2 FAUX   = "+str(res[1]))
