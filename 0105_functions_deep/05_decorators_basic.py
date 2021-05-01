import requests
from test_decorator import timer, uppercase


urls = ['https://api.github.com',
        'https://google.com/',
        'https://100ballov.by',
        'https://www.theverge.com',
        'https://www.buzzfeed.com']


@timer
def connect(url):
    res = requests.get(url)
    return res.status_code


for url in urls:
    connect(url)


@uppercase
def hello():
    return 'hello!'


@uppercase
def post():
    return f'''
    Demid Raksin,
    Belarus, Minsk, Minsk dist.,
    20080, Kiseleva 12, apt. 20'''

print(hello())
print(post())