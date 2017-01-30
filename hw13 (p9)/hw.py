import re

def find_programmirovat(a):
    c = []
    with open (a, 'r', encoding='utf-8') as f:
        for word in f.read().lower().split():
            if re.search('программир(ова(в(ш(ую(ся)?|ая(ся?)|е(м(у)?(ся)?|й(ся)?|е(ся)?|го(ся?))|и(сь|й(ся)?|е(ся)?|х(ся?)|м(и)?(ся)?)?))|л(ся|а(сь)?|о(сь)?|и(сь)?)?|ть(ся)?|нн(ую|ая|о(м(у)?|й|е|го)|ы(й|е|х|м(и)?)))|у(ют?|е(м(ую|ая|о(м(у)?|й|е|го)|ы(й|е|х|м(и)?))|шь|т(ся|е(сь)?)?)|я(сь)?|й(ся|(те(сь)?)?)))', word):
                if word not in c:
                    c.append(word)            
    print(', '.join(c))
    return


find_programmirovat('file.txt')
