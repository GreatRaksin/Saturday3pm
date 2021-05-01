# Функции могут быть вложенными
def speak(text):
    def whisper(t):
        return t.lower() + '...'
    return whisper(text)


print(speak('HELLO'))

