import re

morph = []
count = []
count_i = 0
with open ('F.xml', 'r', encoding='utf-8') as f:
    for line in f.readlines():
        b = re.findall('<w lemma=".+?" type="([A-Za-z0-9]+)', line)
        if b != [] and morph.count(' '.join(b))==0:
            morph.append(' '.join(b))
    for index in morph:
        for line in f.readlines():
            if re.search(index, line):
                count_i += 1
        count.append(count_i)
slovar = dict(zip(morph, count))
print(slovar)
