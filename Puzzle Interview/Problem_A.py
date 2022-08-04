from itertools import combinations, permutations

def replacements(): 
    for comb in combinations(range(10), 8): 
        for perm in permutations(comb): 
            if perm[0] * perm[1] != 0: 
                yield dict(zip('SMENDORY', perm))

def main(a,b,c):
    count= 0
    for replacement in replacements(): 
        f = lambda x: sum(replacement[e] * 10**i for i, e in enumerate(x[::-1])) 
        if f(a) + f(b) == f(c):
            print("Solution Found : ")
            print('{} + {} = {}'.format(f(a), f(b), f(c)))
            count=count+1
            break
    if(count==0):
        print("No Solution")

if __name__ == "__main__":
    a ='SEND' 
    b = 'MORE'
    c = 'MONEY'
    # a = input("Enter a word like SEND = ")
    # b = input("Enter a word like MORE = ")
    # c = input("Enter a word like MONEY = ")
    main(a,b,c)
    