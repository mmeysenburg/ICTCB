n = int(input())
# outputs the number of adventures

for i in range(n):
    a = input()
    # outputs the sequence of items and villains
    # $, |, *, t, j, b, .

    Bag = []
    ok = True
    
    for x in a:
        if x == '$':
            Bag.append('$')

        elif x == '|':
            Bag.append('|')

        elif x == '*':
            Bag.append('*')


        elif x == 't':
            if len(Bag) > 0 and Bag[-1] == '|':
                Bag.pop()
            else:
                ok = False
                break

        elif x == 'j':
            if len(Bag) > 0 and Bag[-1] == '*':
                Bag.pop()
            else:
                ok = False
                break
            
        elif x == 'b':
            if len(Bag) > 0 and Bag[-1] == '$':
                Bag.pop()
            else:
                ok = False
                break
        
    if len(Bag) == 0 and ok:
        print('YES')
    else:
        print('NO')

    #https://www.geeksforgeeks.org/stack-in-python