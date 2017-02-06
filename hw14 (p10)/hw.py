import re

a = input ('File name: ')
with open (a, 'r', encoding='utf-8') as f:
    b = re.findall('Преподаватели</th>\n<td class="" style="padding:0.25em 0.5em; font-size:100%;">\n<p>([0-9 ]+)', f.read())
print (' '.join(b))
