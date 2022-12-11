

file_test = open("2022/data/2022-11-test.txt")
lines_test = file_test.readlines()
file = open("2022/data/2022-11.txt")
lines = file.readlines()


class Monkey:
    def __init__(self, lines):
        self.number = lines[0].split(' ')[1].split(':')[0]
        self.items = [int(i) for i in lines[1].split(':')[1].split(',')]
        self.operation = lines[2].split(':')[1].split('=')[1]
        self.divisible = int(lines[3].split('by')[1])
        self.if_true = int(lines[4].split('monkey')[1])
        self.if_false = int(lines[5].split('monkey')[1])
        self.items_inspected = 0
        #print("{} {} {} {} {} {}".format(self.number, self.items,
        #      self.operation, self.divisible, self.if_true, self.if_false))

    def evaluate(self):
        items_thrown = []
        for item in self.items:
            self.items_inspected += 1
            old = item
            new_item = eval(self.operation)
            new_item = int(new_item/3)
            if (new_item % self.divisible) == 0:
                items_thrown.append((self.if_true, new_item))
            else:
                items_thrown.append((self.if_false, new_item))
        self.items = []

        return items_thrown

    def evaluate_2(self):
        items_thrown = []
        for item in self.items:
            self.items_inspected += 1
            
            # si c'est une multiplication
            if "*" in self.operation:
                old = item 

                # si l'ancien est divisible alors on le fait sur le old qui doit etre plus petit
                if (old % self.divisible) == 0:
                    old = old // self.divisible
                    new_item = eval(self.operation)
                    items_thrown.append((self.if_true, new_item))                 
                else:
                    new_item = eval(self.operation)
                    items_thrown.append((self.if_false, new_item))            
            else:
                old = item 
                new_item = eval(self.operation)
                if (new_item % self.divisible) == 0:
                    new_item = new_item//self.divisible
                    items_thrown.append((self.if_true, new_item))
                else:
                    items_thrown.append((self.if_false, new_item))

        self.items = []

        return items_thrown

    def __str__(self) -> str:
        return "{} {} {} {} {} {}".format(self.number, self.items, self.operation, self.divisible, self.if_true, self.if_false)


def monky_business(lines):
    monkeys = [Monkey(lines[i:i+7]) for i in range(0, len(lines), 7)]
    for i in range(20):
        for monkey in monkeys:
            items_to_move = monkey.evaluate()
            for item in items_to_move:
                monkeys[item[0]].items.append(item[1])

    print(sorted([monkey.items_inspected for monkey in monkeys])[-2:])
    return sorted([monkey.items_inspected for monkey in monkeys])[-2]*sorted([monkey.items_inspected for monkey in monkeys])[-1]


print("PART 1 TEST  : 10605 =? {}".format(monky_business(lines_test)))
print("PART 1 PUZZLE: {}".format(monky_business(lines)))


def monky_business_2(lines):
    monkeys = [Monkey(lines[i:i+7]) for i in range(0, len(lines), 7)]
    for i in range(20):
        print('-- {} ---'.format(i))

        for monkey in monkeys:
            items_to_move = monkey.evaluate_2()
            for item in items_to_move:
                monkeys[item[0]].items.append(item[1])
        for monkey in monkeys:
            print(monkey.items_inspected)

    return sorted([monkey.items_inspected for monkey in monkeys])[-2]*sorted([monkey.items_inspected for monkey in monkeys])[-1]


print("PART 2 TEST (UNFINISHED) : 2713310158 =? {}".format(monky_business_2(lines_test)))
# en vrai, ça donne pas la bonne répone mais close enough
#print("PART 2 PUZZLE: {}".format(result_2(signal(lines))))
