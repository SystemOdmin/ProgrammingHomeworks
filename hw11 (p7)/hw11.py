##def rechood(line):
##    c = line.find('hood')
##    d = []
##    if c != -1:
##        a = line[line[0:c].rfind(' ')+1:c]
##        b = a[c:
##        


with open ('a.txt', 'r', encoding='utf-8') as f:
    b = 0
    d = []
    min = 0
    for line in f.readlines():
        a = (line.count('hood') - line.count (' hood'))
        b += a
        c = line.find('hood')
        if c != -1:
            d.append(line[line[0:line.find('hood')].rfind(' ')+1:line.find('hood')])
min = d.count(d[0])
for i in d:
    if d.count(i) < min:
        min = d.count(i)
for j in d:
    if d.count(j) == min:
        e = j
print (b, ', '.join(d), e, sep='\n')
        
