# following along with the video tutorial
import os, random

if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')

# master list of all possible words
MASTER_LIST = (
    'incomprehensibilities',
    'strengths',
    'unimaginatively',
    'uncopyrightable',
)

def prompt_for_words(challenge_word):
    guesses = set()
    print('What words can you find in "{}"?'.format(challenge_word))
    print('(Enter \'Q\' to \'QUIT\')')
    while True:
        guess = input('{} words > '.format(len(guesses)))
        if guess.lower() == 'q':
            break
        else:
            guesses.add(guess)
    return guesses


# current_word = MASTER_LIST[random.randrange(len(MASTER_LIST))]
current_word = random.choice(MASTER_LIST)
# print(current_word)

user_1_guesses = prompt_for_words(current_word)
user_2_guesses = prompt_for_words(current_word)

print('-' * 10)
print('Player 1 Results:')
player_1_unique = user_1_guesses - user_2_guesses
print('{} balls.'.format(len(player_1_unique) * 5))

print('-' * 10)
print('Player 2 Results:')
player_2_unique = user_2_guesses - user_1_guesses
print('{} balls.'.format(len(player_2_unique) * 5))
