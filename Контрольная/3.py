a = [] 
s = input("Введите слово ")
while s != (""):
    a.append(s)
    s = input("Введите слово ")
with open ('quotes.txt', 'r', encoding='utf-8') as f:
    for i in a:
        print(i)
        for line in f.readlines():
            b = line.split()
            for word in b:
                if word == i:
                    print(line)
                else:
                    continue
