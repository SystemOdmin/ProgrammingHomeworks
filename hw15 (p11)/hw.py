import re
a = input ('File name: ')
with open (a, 'r', encoding='utf-8') as f:
    b = f.read()
    c = re.sub('язык', 'шашлык', b)
    d = re.sub('Язык', 'Шашлык', c)
with open (a, 'w', encoding='utf-8') as f:
    f.write(d)
