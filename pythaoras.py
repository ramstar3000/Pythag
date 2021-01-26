from math import gcd

def pythagoras(x:int):

    triples= []
    
    for m in range(x):
        for n in range(x):

            a = 2 * m * n
            b = m**2 - n**2
            c = m**2 + n**2

            if a>0 and b>0 and c>0:

                if a>b:  triples.append([b,a,c])
                else:    triples.append([a,b,c])

    print(len(triples))
    return triples


def no_repeats(listl:list):
    orig = set()
    for item in listl:
        a,b,c = item
        d = (gcd(a,gcd(b,c)))
        new = (a//d,b//d,c//d)
        orig.add(new)

    print(len(orig))
    return (sorted(orig))

def pprint(listl:list):
    for _ in listl:
        print(f'{_[0]} {_[1]} -> {_[2]}')

some = pythagoras(25)
less = no_repeats(some)
pprint(less)





'''
10 --->  36 , 18
15 --->  91 , 43
20 --->  171, 78


'''
