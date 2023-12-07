
# cartes
cards = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
cards2 = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']
# mains rangées 
types = {
    5: 7,
    4: 6,
    "Full": 5,
    3: 4,
    "2P": 3,
    2: 2,
    1: 1
}

# quoi que c'est, mais avec les jokers
def identify_nature2(hand):

    hand_dict = {}
    for card in cards:
        hand_dict[card] = hand.count(card)

    j_number = hand_dict.pop('J')
    numerous_cards_count = sorted(hand_dict.values())[-1]

    numerous_cards_count += j_number

    if numerous_cards_count == 5 or numerous_cards_count == 4 or numerous_cards_count == 1:
        return types[numerous_cards_count]
    if numerous_cards_count == 3:
        if sorted(hand_dict.values())[-2] == 2:
            return types["Full"]
        else:
            return types[3]
    if numerous_cards_count == 2:
        if sorted(hand_dict.values())[-2] == 2:
            return types["2P"]
        else:
            return types[2]

# quoi que c'est comme carte
def identify_nature(hand):

    hand_dict = []
    
    for card in cards:
        hand_dict.append(hand.count(card))

    numerous_cards_count = sorted(hand_dict)[-1]

    # si full ou carre ou carte haute, pas de doute
    if numerous_cards_count == 5 or numerous_cards_count == 4 or numerous_cards_count == 1:
        return types[numerous_cards_count]

    # si brelan, brelan ou full
    if numerous_cards_count == 3:
        if sorted(hand_dict)[-2] == 2:
            return types["Full"]
        else:
            return types[3]

    # si paires
    if numerous_cards_count == 2:
        if sorted(hand_dict)[-2] == 2:
            return types["2P"]
        else:
            return types[2]

# comparaison pour tri a bulle, partie 2
def compare2(hand1, hand2):

    nature_h1 = identify_nature2(hand1)
    nature_h2 = identify_nature2(hand2)
    
    if nature_h1 != nature_h2:
        return nature_h1 < nature_h2
    else:
        for i in range(0, 5):
            # logique inversée sur mes cartes
            card1 = cards2.index(hand1[i])
            card2 = cards2.index(hand2[i])
            if card1 != card2:
                return card1 > card2

# comparaison pour tri a bulle, partie 1
def compare(hand1, hand2):
    nature_h1 = identify_nature(hand1)
    nature_h2 = identify_nature(hand2)
    if nature_h1 != nature_h2:
        return nature_h1 < nature_h2
    else:
        for i in range(0, 5):
            # logique inversée sur mes cartes
            card1 = cards.index(hand1[i])
            card2 = cards.index(hand2[i])
            if card1 != card2:
                return card1 > card2

def score(lines,compare_f):
    
    hands = [line.strip().split(' ') for line in lines]
    solution1 = 0
    i = len(hands)
    for hand in bubble_sort(hands, compare_f):
        solution1 += i*int(hand[1])
        i -= 1
    return solution1
    
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

# TU aoc
test1 = "\
32T3K 765;\
T55J5 684;\
KK677 28;\
KTJJT 220;\
QQQJA 483"

# autre test trouve sur reddit, mais mon erreur était ailleurs...
test2 = "2345A 1;\
Q2KJJ 13;\
Q2Q2Q 19;\
T3T3J 17;\
T3Q33 11;\
2345J 3;\
J345A 2;\
32T3K 5;\
T55J5 29;\
KK677 7;\
KTJJT 34;\
QQQJA 31;\
JJJJJ 37;\
JAAAA 43;\
AAAAJ 59;\
AAAAA 61;\
2AAAA 23;\
2JJJJ 53;\
JJJJ2 41"
file = open("2023/data/2023-7.txt")
lines = file.readlines()

print("UTEST 33332 < 2AAAA is False=" + str(compare("33332", "2AAAA")))
print("UTEST 77888 < 77788 is False=" + str(compare("77888", "77788")))
print("UTEST JJJTT < Q2226 is False=" + str(compare("JJJTT", "JQAQQ")))

print("UTEST nat of JJTTT 7=" + str(identify_nature2("JJJTT")))
print("UTEST nat of QJJQ2 6=" + str(identify_nature2("QJJQ2")))
print("UTEST JKKK2<QQQQ2   = " + str(compare2("JKKK2", "QQQQ2")))

print("TEST1 6440          = " + str(score(test1.split(';'),compare)))

print("TEST2 5905          = " + str(score(test1.split(';'),compare2)))

print("TEST1 bis 6592      = "+str(score(test1.split(';'),compare)))
print("TEST2 bis 6839      = "+str(score(test1.split(';'),compare2)))
print("TOTAL1 253603890    = "+str(score(lines,compare)))
print("TOTAL2 253630098    = "+str(score(lines,compare2)))
