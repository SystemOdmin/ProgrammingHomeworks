import re

a = input ('File name: ')
with open (a, 'r', encoding='utf-8') as f:
    b = re.findall('Преподаватели<.+?>\n<.+?>\n<p>([0-9 ]+)', f.read())
with open ('prepody.txt', 'w', encoding='utf-8') as g:
    c =' '.join(b)
    g.write(c)
