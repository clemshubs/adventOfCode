file_test = open("2022/data/2022-8-test.txt")
lines_test = file_test.readlines()
file = open("2022/data/2022-8.txt")
lines = file.readlines()


def get_forest(lines):
    forest = []
    for line in lines:
        forest.append(list(line.strip('\n')))
    return forest


def get_visibles(forest):
    visible_trees = set()

    # les cotes
    visible_trees.update([(0, k, int(forest[0][k]))
                         for k in range(0, len(forest[0]))])

    visible_trees.update([(len(forest)-1, k, int(forest[len(forest)-1][k]))
                         for k in range(0, len(forest[0]))])

    visible_trees.update([(k, 0, int(forest[k][0]))
                         for k in range(0, len(forest))])
    visible_trees.update([(k, len(forest[k])-1, int(forest[k][len(forest[0])-1]))
                         for k in range(0, len(forest))])

    print("Cotes : {} == {}".format(len(forest) *
          2+len(forest[0])*2-4, len(visible_trees)))
    # i est la ligne, j la colone. donc on regarde de gauche à droite
    for i in range(0, len(forest)):
        visible_tree = (i, 0, int(forest[i][0]))
        for j in range(0, len(forest[0])):
            if int(forest[i][j]) > visible_tree[2]:
                #print("Added {} {} of height {}".format(i,j,int(forest[i][j])))
                visible_tree = (i, j, int(forest[i][j]))
                visible_trees.add(visible_tree)

                # print(visible_trees)

                #print("len {}, added {} ".format(len(visible_trees),visible_tree))

        visible_tree = (i, len(forest[i])-1, int(forest[i][len(forest[i])-1]))
        for j in reversed(range(0, len(forest[0]))):
            #print("{} {}".format(i,j))
            if int(forest[i][j]) > visible_tree[2]:
                #print("Added {} {} of height {}".format(i,j,int(forest[i][j])))
                visible_tree = (i, j, int(forest[i][j]))
                visible_trees.add(visible_tree)
                #print("len {}, added {} ".format(len(visible_trees),visible_tree))


##### i devient la colonne eet j la ligne
    # donc on regarde de bas en haut
    for i in range(0, len(forest[0])):
        visible_tree = (0, i, int(forest[0][i]))
        # pour chaque colonne
        for j in range(0, len(forest)):
            if int(forest[j][i]) > visible_tree[2]:
                #print("Added {} {}".format(j,i))
                visible_tree = (j, i, int(forest[j][i]))
                visible_trees.add(visible_tree)

                # print(len(visible_trees))

        visible_tree = (len(forest[0])-1, i, int(forest[len(forest[0])-1][i]))
        for j in reversed(range(0, len(forest))):
            if int(forest[j][i]) > visible_tree[2]:
                #print("Added {} {}".format(j,i))
                visible_tree = (j, i, int(forest[j][i]))
                visible_trees.add(visible_tree)
                # print(len(visible_trees))

    return len(visible_trees)


    # bas
    # #gauche
    # droit

print("TEST 21 = {}".format(get_visibles(get_forest(lines_test))))

print("PUZZLE xxx = {}".format(get_visibles(get_forest(lines))))
print("wrong : 1803")

def get_visibles_2(forest):
    HScore=0
    # on parcoure la foret
    for k in range(0,len(forest)):
        for n in range(0,len(forest[0])):
            score = score_of_tree(k,n,forest)
            

            if score > HScore:
                HScore=score

    return HScore

def score_of_tree(k,n,forest):
    score=1
# i est la ligne, j la colone. donc on regarde de gauche à droite
    height=int(forest[k][n])


    # vers le haut
    
    i=0
    while (k-i-1)>=0:
        if int(forest[k-i-1][n])<height :
            i+=1
        elif int(forest[k-i-1][n])>=height :
            i+=1
            break
    score*=max(1,i)

    # gauche
    i=0
    while (n-i-1)>=0:        
        if int(forest[k][n-i-1])<height :
            i+=1
        elif int(forest[k][n-i-1])>=height :
            i+=1
            break

    score*=max(1,i)

    # droite
    i=0
    while i+n+1<(len(forest[0])):
        if int(forest[k][n+i+1])<height :
            i+=1
        elif int(forest[k][n+i+1])>=height :
            i+=1
            break
    score*=max(1,i)
    
    
    # vers le bas
    i=0
    while i+k+1<(len(forest)) :
        if int(forest[k+i+1][n])<height :
            i+=1
        elif int(forest[k+i+1][n])>=height :
            i+=1
            break    
    score*=max(1,i)

    return score

print(" 4 == {}".format(score_of_tree(1,2,get_forest(lines_test))))
print(" 8 == {}".format(score_of_tree(3,2,get_forest(lines_test))))

print(" 479400 = {}".format(str(get_visibles_2(get_forest(lines)))))


