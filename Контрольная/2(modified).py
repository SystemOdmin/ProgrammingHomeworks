b = 0
d = []
with open ('quotes.txt', 'r', encoding='utf-8') as f:
    for line in f.readlines():
        a = line.split()
        for word in a:
            if word == 'Разум' or word == 'разум':
                b+=1
                c = line.split('—')
                d.append(c[1].rstrip('\n'))
                break
            else:
                continue
print(b)
print(', '.join(d))
