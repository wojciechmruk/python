from random import randrange

max_tries = 5
tries = 0
words = ['cow', 'dog', 'cat', 'fish', 'horse', 'rabbit', 'hen', 'hamsters', 'duck']
word = words[randrange(10)]
guess = ''
used_letters = ''

for _ in range(0, len(word)):
    guess += '_'


def update_guess(l, guess_word):
    if l in word:
        for x in range(0, len(guess_word)):
            if word[x] == l:
                s = list(guess_word)
                s[x] = l
                guess_word = ''.join(s)
    return guess_word


while tries < 5:
    print('\n' + guess)
    print('Used letters: ' + used_letters)
    letter = input("Enter a letter:")[0]

    if letter in used_letters:
        print('Already used. Try again')
        continue
    else:
        used_letters += letter + ' '

    if letter in word:
        guess = update_guess(letter, guess)
    else:
        tries += 1

    if word == guess:
        print('BRAVO!!!')
        exit()

print('Sorry, you lose.')
