import random

def noun():
    with open ('nouns.txt', 'r', encoding='utf-8') as f:
        a = []
        for line in f.readlines():
            a.append(line.strip('\n'))
    return random.choice(a)

def adjective():
    with open ('adjectives.txt', 'r', encoding='utf-8') as f:
        a = []
        for line in f.readlines():
            a.append(line.strip('\n'))
    return random.choice(a)

def adverb():
    with open ('adverbs.txt', 'r', encoding='utf-8') as f:
        a = []
        for line in f.readlines():
            a.append(line.strip('\n'))
    return random.choice(a)

def intransitive():
    with open ('verbs_intransitive.txt', 'r', encoding='utf-8') as f:
        a = []
        for line in f.readlines():
            a.append(line.strip('\n'))
    return random.choice(a)

def transitive():
    with open ('verbs_transitive.txt', 'r', encoding='utf-8') as f:
        a = []
        for line in f.readlines():
            a.append(line.strip('\n'))
    return random.choice (a)

def object_adjective():
    with open ('object_adjectives.txt', 'r', encoding='utf-8') as f:
        a = []
        for line in f.readlines():
            a.append(line.strip('\n'))
    return random.choice (a)

def direct_object():
    with open ('direct_objects.txt', 'r', encoding='utf-8') as f:
        a = []
        for line in f.readlines():
            a.append(line.strip('\n'))
    return random.choice (a)

def no():
    a = [' не ', ' ', ' ', ' ', ' ']
    return random.choice(a)

def statement():
    a = adjective() + ' ' + noun() + no() + transitive() + ' ' + object_adjective() + ' ' + direct_object() + '.'
    b = adjective() + ' ' + noun() + no() + transitive() + ' ' + object_adjective() + ' ' + direct_object() + '!'
    c = adjective() + ' ' + noun() + no() + intransitive() + ' ' + adverb() + '.'
    d = adjective() + ' ' + noun() + no() + intransitive() + ' ' + adverb() + '!'
    x = [a, b, c, d]
    return random.choice(x)

def question():
    a = adverb() + ' ' + 'ли ' + adjective() + ' ' + noun() + ' ' + transitive() + ' ' + object_adjective() + ' ' + direct_object() + '?'
    b = adverb() + ' ' + 'ли ' + adjective() + ' ' + noun() + ' ' + intransitive() + '?'
    c = transitive() + ' ' + 'ли ' + adjective() + ' ' + noun() + ' ' + object_adjective() + ' ' + direct_object() + '?'
    d = intransitive() + ' ' + 'ли ' + adjective() + ' ' + noun() + '?'
    x = [a, b, c, d]
    return random.choice(x)

def sentence():
    x = statement()
    y = statement()
    z = question()
    w = [x, y, z]
    return random.choice (w)

def generate():
    a = []
    for x in range(5):
        a.append(sentence().capitalize())
    print (' '.join(a))
    return

generate()
