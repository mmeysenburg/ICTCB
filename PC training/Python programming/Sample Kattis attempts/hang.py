word = set(input())
guesses = input()

bad = 0
for x in guesses:

    if x in word:
        word.remove(x)
        if len(word) == 0:
            print('WIN')
            break
    else:
        bad += 1
        if bad == 10:
            print('LOSE')
            break