with open ('quotes.txt', 'r', encoding='utf-8') as f:
    for line in f.readlines():
        a = line.split()
        if len(a) > 10:
            print(' '.join(a))
        else:
            continue
