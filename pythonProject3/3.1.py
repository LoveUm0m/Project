engtorus = {
    'one' : 'один',
    'two' : 'два',
    'three': 'три',
    'four' : 'четыре',
    'five' : 'пять',
    'six': 'шесть',
    'seven' : 'семь',
    'eight' : 'восемь',
    'nine': 'девять',
    'ten' : 'десять',
}

def translat(eng):
    return engtorus.get(eng)
print(translat('four'))