import re

morph = []
count = []
with open ('F.xml', 'r', encoding='utf-8') as f:
    for line in f.readlines():
        b = re.findall('<w lemma=".+?" type="([A-Za-z0-9þ]{2,})', line)
        if b != [] and morph.count(' '.join(b))==0:
            morph.append(' '.join(b))
    f.seek(0,0)
    morph.append('c')
    for i in morph:
        count_i = 0
        for line in f.readlines():
            if re.findall('<w lemma=".+?" type="(' + i + ')', line):
                count_i += 1
        f.seek(0,0)
        count.append(count_i)
slovar = dict(zip(morph, count))
with open ('information.txt', 'a', encoding='utf-8') as g:
    for key in slovar:
        g.write(key + ' ' + str(slovar[key]) + '\n')
