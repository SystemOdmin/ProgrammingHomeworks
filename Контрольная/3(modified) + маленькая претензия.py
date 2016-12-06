a = []
d = 0
s = input("Введите слово ")
while s != (""):
    a.append(s)
    s = input("Введите слово ")
with open ('quotes.txt', 'r', encoding='utf-8') as f:
    for i in a:
        print('\n', i, '\n')
##f.seek(0,0) - функция, которую мы не проходили
##без знания того, как это работает, нахождение ошибки в этом цикле мне не представляется возможным
        f.seek(0,0)
        for line in f.readlines():
            b = line.count(i)
            d += b
            c = line.split()
            for word in c:
                if word == i:
                    print(line)
        if d == 0:
            print('Цитат не нашлось')
        d = 0
