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



def _ppcm(a, b):
    Da = decomp(a)
    Db = decomp(b)
    p = 1
    for facteur, exposant in Da.items():
        if facteur in Db:
            exp = max(exposant, Db[facteur])
        else:
            exp = exposant

        p *= facteur**exp

    for facteur, exposant in Db.items():
        if facteur not in Da:
            p *= facteur**exposant

    return p

def decomp(n):
    L = dict()
    k = 2
    while n != 1:
        exp = 0
        while n % k == 0:
            n = n // k
            exp += 1
        if exp != 0:
            L[k] = exp
        k = k + 1
        
    return L

def ppcm(*args):
    L = list(args)
    if len(L) == 2:
        return _ppcm(L[0], L[1])
    else:
        n = len(L)
        i = 0
        A = []
        while i <= n-2:
            A.append(_ppcm(L[i], L[i+1]))
            i += 2

        if n % 2 != 0:
            A.append(L[n-1])

        return ppcm(*A)

#ajouter a* et autres trucs qui servent