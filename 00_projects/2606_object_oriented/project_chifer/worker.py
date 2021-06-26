import string


class Caesar:
    key = 3

    def __init__(self, msg):
        self.message = msg
        self.symbols = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдежзийклмнопрстуфхцчшщъыьэюя'

    def set_language(self, lang):
        if lang.lower().startswith('ru'):
            self.symbols = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдежзийклмнопрстуфхцчшщъыьэюя'
        elif lang.lower().startswith('en'):
            self.symbols = string.ascii_letters
        else:
            print('Not available language')
        return self.symbols

    def encrypt(self, key):
        '''Метод шифроки сообщения с определенным сдвигом'''
        tr = ''  # здесь храним зашифрованное сообщение
        for symbol in self.message:
            symbolIndex = self.symbols.find(symbol)
            if symbolIndex == -1:  # символ не найден
                # просто добавить этот символ без изменений
                tr += symbol
            else:  # Зашифровать или расшифровать
                symbolIndex += key

                if symbolIndex >= len(self.symbols):
                    symbolIndex -= len(self.symbols)
                elif symbolIndex < 0:
                    symbolIndex += len(self.symbols)

                tr += self.symbols[symbolIndex]
        return tr


