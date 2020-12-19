from random import *


HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

# Word bank of animals
words = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()


def getRandomWord(wordList):
    """Возвращает случайно выбранное слово из списка слов"""
    wordIndex = randint(0, len(wordList) - 1)
    return words[wordIndex]


# print(getRandomWord(words)) <- проверить, что функция работает
def displayBoard(errorLetters, correctLetters, secretWord):
    """Отображает игровое поле игры 'Виселица'"""
    print(HANGMANPICS[len(errorLetters)])
    print('Неправильные буквы: ')
    for letter in errorLetters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(secretWord)
    for letter in range(len(secretWord)):
        if secretWord[letter] in correctLetters:
            blanks = blanks[:letter] + secretWord[letter] + blanks[letter + 1:]

    for letter in blanks:
        print(letter, end=' ')

    print()



def getGuess(alreadyGuessed):
    """Возвращает букву, введенную игроком. Проверяет, что была введена только 1 буква"""
    while True:
        guess = input('Введите букву: ').lower()

        if len(guess) != 1:  # если буква не одна
            print('Введите ОДНУ букву!')
        elif guess in alreadyGuessed:  # если угадана
            print('Вы уже называли эту букву!')
        elif guess.isdigit() or guess.isspace():  # если число или пробел
            print('Введите одну БУКВУ')
        else:
            return guess


def playAgain():
    """Возвращает TRUE, если игрок хочет играть еще"""
    return input('Хотите сыграть еще раз? ').lower().startswith(('д', 'l', 'y'))


errorLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)
gameIsDone = False

while True:
    displayBoard(errorLetters, correctLetters, secretWord)

    guess = getGuess(errorLetters + correctLetters)
    if guess in secretWord:
        correctLetters += guess

        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print(f'Вы угадали! Это было слово {secretWord}.')
            gameIsDone = True
    else:
        errorLetters += guess
        if len(errorLetters) == len(HANGMANPICS) - 1:
            displayBoard(HANGMANPICS, errorLetters, correctLetters, secretWord)
            print(f'Ошибок: {len(errorLetters)}, правильных: {len(correctLetters)}, слово: {secretWord}')
            gameIsDone = True



