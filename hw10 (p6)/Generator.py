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
    a = [' не ', ' ', ' ', ' ', ' ']
    return random.choice(a)

def statement():
    a = adjective() + ' ' + noun() + no() + transitive() + ' ' + object_adjective() + ' ' + direct_object() + '.'
    b = adjective() + ' ' + noun() + no() + intransitive() + ' ' + adverb() + '.'
    x = [a, b]
    return random.choice(x)

def exclamation():
    a = adjective() + ' ' + noun() + no() + intransitive() + ' ' + adverb() + '!'
    b = adjective() + ' ' + noun() + no() + transitive() + ' ' + object_adjective() + ' ' + direct_object() + '!'
    x = [a, b]
    return random.choice(x)
    
def question():
    a = adverb() + ' ' + 'ли ' + adjective() + ' ' + noun() + ' ' + transitive() + ' ' + object_adjective() + ' ' + direct_object() + '?'
    b = adverb() + ' ' + 'ли ' + adjective() + ' ' + noun() + ' ' + intransitive() + '?'
    c = transitive() + ' ' + 'ли ' + adjective() + ' ' + noun() + ' ' + object_adjective() + ' ' + direct_object() + '?'
    d = intransitive() + ' ' + 'ли ' + adjective() + ' ' + noun() + '?'
    x = [a, b, c, d]
    return random.choice(x)

def condition():
    a = 'Если ' + adjective() + ' ' + noun() + no() + transitive() + ' ' + object_adjective() + ' ' + direct_object() + ', то и ' + adjective() + ' ' + noun() + no() + transitive() + ' ' + object_adjective() + ' ' + direct_object() + '.'
    b = 'Если ' + adjective() + ' ' + noun() + no() + transitive() + ' ' + object_adjective() + ' ' + direct_object() + ', то и ' + adjective() + ' ' + noun() + no() + intransitive() + ' ' + adverb() + '.'
    c = 'Если ' + adjective() + ' ' + noun() + no() + intransitive() + ' ' + adverb() + ', то и ' + adjective() + ' ' + noun() + no() + intransitive() + ' ' + adverb() + '.'
    d = 'Если ' + adjective() + ' ' + noun() + no() + intransitive() + ' ' + adverb() + ', то и ' + adjective() + ' ' + noun() + no() + transitive() + ' ' + object_adjective() + ' ' + direct_object() + '.'
    x = [a, b, c, d]
    return random.choice(x)

def imperative():
    a = (no() + imperative_intransitive() + ',' + adjective() + ' ' + noun() + '.').strip(' ')
    b = (adjective() + ' ' + noun() + ',' + no() + imperative_intransitive() + '.').strip(' ')
    c = (no() + imperative_intransitive() + ', ' + adjective() + ' ' + noun() + '!').strip(' ')
    d = (adjective() + ' ' + noun() + ',' + no() + imperative_intransitive() + '!').strip(' ')
    e = (no() + imperative_transitive() + ' ' + object_adjective() + ' ' + direct_object() + ', ' + adjective() + ' ' + noun() + '.').strip(' ')
    f = (adjective() + ' ' + noun() + ',' + no() + imperative_transitive() + ' ' + object_adjective() + ' ' + direct_object() + '.').strip(' ')
    g = (no() + imperative_transitive() + ' ' + object_adjective() + ' ' + direct_object() + ', ' + adjective() + ' ' + noun() + '!').strip(' ')
    h = (adjective() + ' ' + noun() + ',' + no() + imperative_transitive() + ' ' + object_adjective() + ' ' + direct_object() + '!').strip(' ')
    x = [a, b, c, d, e, f, g, h]
    return random.choice(x)

def generate():
    a = statement().capitalize()
    b = exclamation().capitalize()
    c = question().capitalize()
    d = condition()
    e = imperative().capitalize()
    w = [a, b, c, d, e]
    random.shuffle (w)
    print (' '.join(w))
    return

generate()
