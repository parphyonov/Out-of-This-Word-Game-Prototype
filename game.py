import os

if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')

longword = 'Novosibirsk'.lower()
# longword = input('Provide us with some really long word. The longer the word, the more words it may contain! ')

lset = set(longword)

while True:

    print()
    print('=== Submit \'quit\' to stop providing more words. ===')
    print()

    guess = input('And your word is? ').lower()
    gset = set(guess)

    if guess.lower() == 'quit':
        break
    else:
        if not gset - lset:
            print('Yep!')
        else:
            print('Nope!')

print()
