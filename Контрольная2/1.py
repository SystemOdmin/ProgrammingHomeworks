import re

a = 0
with open ('F.xml', 'r', encoding='utf-8') as f:
    for line in f.readlines():
        a +=1
        if re.search(r'</teiHeader>', line):
            break
with open ('information.txt', 'w', encoding='utf-8') as g:
    g.write(str(a) + '\n')
