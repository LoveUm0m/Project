import random
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

def get_jokes(num):
    jokelist = []
    for i in range(num):
        cur_nouns = random.choice(nouns)
        cur_adverbs = random.choice(adverbs)
        cur_adjectives = random.choice(adjectives)
        jokelist.append(f'{cur_nouns} {cur_adverbs} {cur_adjectives}')
    return jokelist
print(get_jokes(1))
print(get_jokes(2))