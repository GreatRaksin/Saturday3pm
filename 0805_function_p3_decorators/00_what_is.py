def uppercase(func):
    def wrapper():
        orig_res = func()
        modif_res = orig_res.upper()
        return modif_res
    return wrapper


def strong(func):
    def wrapper():
        return '<strong>' + func() + '</strong>'
    return wrapper


def emphasis(func):
    def wrapper():
        return '<em>' + func() + '</em>'
    return wrapper


@strong
@emphasis
@uppercase
def text():
    return 'some text'


print(text())
#print(uppercase)
#print(uppercase(text))
