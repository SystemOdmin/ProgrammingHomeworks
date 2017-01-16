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

def imperative_intransitive():
    with open ('imperatives_intransitive.txt', 'r', encoding='utf-8') as f:
        a = []
        for line in f.readlines():
            a.append(line.strip('\n'))
    return random.choice (a)

def imperative_transitive():
    with open ('imperatives_transitive.txt', 'r', encoding='utf-8') as f:
        a = []
        for line in f.readlines():
            a.append(line.strip('\n'))
    return random.choice (a)

def no():
    a = [' не ']
    return random.choice(a)

def statement():
    a = adjective() + ' ' + noun() + ' ' + transitive() + ' ' + object_adjective() + ' ' + direct_object() + '.'
    b = adjective() + ' ' + noun() + ' ' + intransitive() + ' ' + adverb() + '.'
    c = adjective() + ' ' + noun() + ' ' + transitive() + ' ' + object_adjective() + ' ' + direct_object() + '!'
    d = adjective() + ' ' + noun() + ' ' + intransitive() + ' ' + adverb() + '!'
    x = [a, b, c, d]
    return random.choice(x)

def negation():
    a = adjective() + ' ' + noun() + no() + intransitive() + ' ' + adverb() + '!'
    b = adjective() + ' ' + noun() + no() + transitive() + ' ' + object_adjective() + ' ' + direct_object() + '!'
    c = adjective() + ' ' + noun() + no() + intransitive() + ' ' + adverb() + '!'
    d = adjective() + ' ' + noun() + no() + transitive() + ' ' + object_adjective() + ' ' + direct_object() + '!'
    x = [a, b, c, d]
    return random.choice(x)
    
def question():
    a = adverb() + ' ' + 'ли ' + adjective() + ' ' + noun() + ' ' + transitive() + ' ' + object_adjective() + ' ' + direct_object() + '?'
    b = adverb() + ' ' + 'ли ' + adjective() + ' ' + noun() + ' ' + intransitive() + '?'
    c = transitive() + ' ' + 'ли ' + adjective() + ' ' + noun() + ' ' + object_adjective() + ' ' + direct_object() + '?'
    d = intransitive() + ' ' + 'ли ' + adjective() + ' ' + noun() + '?'
    x = [a, b, c, d]
    return random.choice(x)

def condition():
    a = 'Если ' + adjective() + ' ' + noun() + ' ' + transitive() + ' ' + object_adjective() + ' ' + direct_object() + ', то и ' + adjective() + ' ' + noun() + ' ' + transitive() + ' ' + object_adjective() + ' ' + direct_object() + '.'
    b = 'Если ' + adjective() + ' ' + noun() + ' ' + transitive() + ' ' + object_adjective() + ' ' + direct_object() + ', то и ' + adjective() + ' ' + noun() + ' ' + intransitive() + ' ' + adverb() + '.'
    c = 'Если ' + adjective() + ' ' + noun() + ' ' + intransitive() + ' ' + adverb() + ', то и ' + adjective() + ' ' + noun() + ' ' + intransitive() + ' ' + adverb() + '.'
    d = 'Если ' + adjective() + ' ' + noun() + ' ' + intransitive() + ' ' + adverb() + ', то и ' + adjective() + ' ' + noun() + ' ' + transitive() + ' ' + object_adjective() + ' ' + direct_object() + '.'
    x = [a, b, c, d]
    return random.choice(x)

def imperative():
    a = imperative_intransitive() + ', ' + adjective() + ' ' + noun() + '.'
    b = adjective() + ' ' + noun() + ', ' + imperative_intransitive() + '.'
    c = imperative_intransitive() + ', ' + adjective() + ' ' + noun() + '!'
    d = adjective() + ' ' + noun() + ', ' + imperative_intransitive() + '!'
    e = imperative_transitive() + ' ' + object_adjective() + ' ' + direct_object() + ', ' + adjective() + ' ' + noun() + '.'
    f = adjective() + ' ' + noun() + ', ' + imperative_transitive() + ' ' + object_adjective() + ' ' + direct_object() + '.'
    g = imperative_transitive() + ' ' + object_adjective() + ' ' + direct_object() + ', ' + adjective() + ' ' + noun() + '!'
    h = adjective() + ' ' + noun() + ', ' + imperative_transitive() + ' ' + object_adjective() + ' ' + direct_object() + '!'
    x = [a, b, c, d, e, f, g, h]
    return random.choice(x)

def generate():
    a = statement().capitalize()
    b = negation().capitalize()
    c = question().capitalize()
    d = condition()
    e = imperative().capitalize()
    w = [a, b, c, d, e]
    random.shuffle (w)
    print (' '.join(w))
    return

generate()
