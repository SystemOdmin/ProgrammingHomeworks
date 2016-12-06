with open ('quotes.txt', 'r', encoding='utf-8') as f:
    for line in f.readlines():
        if len(line) > 10:
            print(line)
        else:
            continue
          
