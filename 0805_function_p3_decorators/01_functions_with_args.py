def proxy(func):
    def wrapper(*args, **kwargs):
        print(f'ТРАССЕР: вызвана функция {func.__name__}()',
              f'с {args}, {kwargs}')
        orig_res = func(*args, **kwargs)

        print(f'ТРАССЕР: функция {func.__name__}()',
              f'вернула "{orig_res}"')
        return orig_res
    return wrapper


@proxy
def say(name, text):
    return f'{name.title()}: {text}'


print(say('demid', 'hello, Python!'))