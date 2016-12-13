with open ('quotes.txt', 'r', encoding='utf-8') as f:
    for line in f.readlines():
        a = line.split('—')[0]
        b = a.split()
        if len(b) > 10:
            print(' '.join(b))
        else:
            continue
