from types import NoneType
from random_word import RandomWords
import os


def show_title():
    os.system('cls')
    print("\n\t*******************************")
    print("\t******** H A N G M A N ********")
    print("\t*******************************")
    print("\t***** Type 'quit' to exit *****")
    print("\t*******************************")


def show_progress(wrong_guesses):
    print('\n\t\t┌──────┐')
    if wrong_guesses == 0:
        print('\t\t│')
        print('\t\t│')
        print('\t\t│')
        print('\t\t│')

    elif wrong_guesses == 1:
        print('\t\t│      │')
        print('\t\t│')
        print('\t\t│')
        print('\t\t│')

    elif wrong_guesses == 2:
        print('\t\t│      │')
        print('\t\t│      O')
        print('\t\t│')
        print('\t\t│')

    elif wrong_guesses == 3:
        print('\t\t│      │')
        print('\t\t│      O')
        print('\t\t│      │')
        print('\t\t│')

    elif wrong_guesses == 4:
        print('\t\t│      │')
        print('\t\t│     ╲O')
        print('\t\t│      │')
        print('\t\t│')

    elif wrong_guesses == 5:
        print('\t\t│      │')
        print('\t\t│     ╲O╱')
        print('\t\t│      │')
        print('\t\t│')

    elif wrong_guesses == 6:
        print('\t\t│      │')
        print('\t\t│     ╲O╱')
        print('\t\t│      │')
        print('\t\t│     ╱')

    elif wrong_guesses == 7:
        print('\t\t│      │')
        print('\t\t│      O')
        print('\t\t│     ╱│╲')
        print('\t\t│     ╱ ╲')

    # print('\t\t|')
    print('\t\t└──────────')


rw = RandomWords()
game_active = True

while game_active:
    guessed_letter = ''
    guessed_letters = ''
    word = None

    while word is None:
        word = rw.get_random_word(
            hasDictionaryDef="true",
            includePartOfSpeech="noun,verb")

    word = word.lower()
    bad_guess = 0

    while guessed_letter != 'quit':
        show_title()

        if guessed_letter not in guessed_letters:
            guessed_letters += guessed_letter
            if guessed_letter not in word:
                bad_guess += 1
                if bad_guess > 6:
                    show_progress(bad_guess)
                    print('\n\tToo many incorrect guesses')
                    print('\n\tThe word was %s' % word)
                    break
        elif guessed_letter != '':
            print('\n\tYou already guessed that letter.')

        print('\n\tIncorrect Guesses: %d' % bad_guess)
        show_progress(bad_guess)
        print('\n\tGuessed Letters: %s' % guessed_letters)
        print('\n\t', end='')

        correct_letters = 0
        for letter in word:
            if letter in guessed_letters or letter in '- ':
                correct_letters += 1
                print('%s ' % letter, end='')
            else:
                print('_ ', end='')
        print()

        if correct_letters == len(word):
            print('\n\tCongratulations, you got them all!')
            break

        guessed_letter = input('\n\tEnter a Letter: ')

    play_again = input('\n\tWould you like to play again? ')

    if play_again != 'y':
        break

print('\n\tGame Over')
