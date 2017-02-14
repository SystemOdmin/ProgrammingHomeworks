import re

pronoun_n = []
corpus = []
corpus1 = []
corpus2 = []
corpus3 = []
with open ('F.xml', 'r', encoding='utf-8') as f:
    for line in f.readlines():
        b = re.findall('<w lemma=".+?" type="f.h.+?">(.+?)</w>', line)
        if b != []:
            pronoun_n.append(' '.join(b))
    f.seek(0,0)
    for line in f.readlines():
        a = re.findall('<w lemma="(.+?)"', line)
        b = re.findall('<w lemma=".+?" type="(.+?)"', line)
        c = re.findall('<w lemma=".+?" type=".+?">(.+?)</w>', line)
        if a != []:
            corpus1.append(a)
            corpus2.append(b)
            corpus3.append(c)
for i in range(len(corpus1)):
    a = ''.join(corpus1[i])
    b = ''.join(corpus2[i])
    c = ''.join(corpus3[i])
    corpus.append(a + ',' + b + ',' + c)
with open ('information.txt', 'a', encoding='utf-8') as g:
    g.write(','.join(pronoun_n))
with open ('corpus.csv', 'w', encoding='utf-8') as e:
    e.write(('\n'.join(corpus)))
