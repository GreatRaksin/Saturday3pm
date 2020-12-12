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
    return wordList[wordIndex]


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

